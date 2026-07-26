// Extracts links, flags duplicates, and optionally live-checks each URL.
"use strict";

const fs = require("fs");

// Accepts scheme://, www., or bare "domain.tld/" links followed by a run
// of non-whitespace/non-bracket characters.
const LINK_RE =
  /(?:https?:\/\/|www\d{0,3}[.]|[a-z0-9.-]+[.][a-z]{2,4}\/)(?:[^\s()<>]+|\([^\s()<>]+\))+(?:\([^\s()<>]+\)|[^\s`!()[\]{};:'".,<>?«»""''])/gi;

const USER_AGENTS = [
  "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
];

const CLOUDFLARE_FLAGS = [
  "403 Forbidden",
  "cloudflare",
  "Cloudflare",
  "Security check",
  "Please Wait... | Cloudflare",
  "We are checking your browser...",
  "Please stand by, while we are checking your browser...",
  "Checking your browser before accessing",
  "This process is automatic.",
  "Your browser will redirect to your requested content shortly.",
  "Please allow up to 5 seconds",
  "DDoS protection by",
  "Ray ID:",
  "Cloudflare Ray ID:",
  "_cf_chl",
  "_cf_chl_opt",
  "__cf_chl_rt_tk",
  "cf-spinner-please-wait",
  "cf-spinner-redirecting",
];

function fakeUserAgent() {
  return USER_AGENTS[Math.floor(Math.random() * USER_AGENTS.length)];
}

function findLinksInText(text) {
  return text.match(LINK_RE) || [];
}

function findLinksInFile(filename) {
  const readme = fs.readFileSync(filename, "utf8");
  const indexAt = readme.indexOf("## Index");
  const content = indexAt === -1 ? readme : readme.slice(indexAt);
  return findLinksInText(content);
}

// Flags a link the first time it's seen again (matches upstream: only the
// *second* occurrence is reported, not every subsequent repeat).
function checkDuplicateLinks(links) {
  const seenCount = new Map();
  const duplicates = [];

  for (const raw of links) {
    const link = raw.replace(/\/+$/, "");
    const count = (seenCount.get(link) || 0) + 1;
    seenCount.set(link, count);
    if (count === 2) duplicates.push(link);
  }

  return { hasDuplicates: duplicates.length > 0, duplicates };
}

function getHostFromLink(link) {
  let host = link.includes("://") ? link.split("://")[1] : link;
  if (host.includes("/")) host = host.split("/")[0];
  else if (host.includes("?")) host = host.split("?")[0];
  else if (host.includes("#")) host = host.split("#")[0];
  return host;
}

async function hasCloudflareProtection(response) {
  const code = response.status;
  const server = response.headers.get("server");
  if ((code === 403 || code === 503) && server === "cloudflare") {
    const html = await response.text().catch(() => "");
    return CLOUDFLARE_FLAGS.some((flag) => html.includes(flag));
  }
  return false;
}

// Returns { hasError, errorMessage } for a single link, mirroring the error
// categories (CLT/SSL/CNT/TMO/UKN) the upstream script reports.
async function checkIfLinkIsWorking(link, { timeoutMs = 25000 } = {}) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const response = await fetch(link, {
      signal: controller.signal,
      redirect: "follow",
      headers: {
        "User-Agent": fakeUserAgent(),
        Host: getHostFromLink(link),
      },
    });

    if (response.status >= 400 && !(await hasCloudflareProtection(response))) {
      return { hasError: true, errorMessage: `ERR:CLT: ${response.status} : ${link}` };
    }
    return { hasError: false, errorMessage: "" };
  } catch (error) {
    if (error.name === "AbortError") {
      return { hasError: true, errorMessage: `ERR:TMO: ${link}` };
    }
    if (error.cause && /certificate|SSL|TLS/i.test(String(error.cause))) {
      return { hasError: true, errorMessage: `ERR:SSL: ${error.message} : ${link}` };
    }
    if (error.code === "ECONNREFUSED" || error.code === "ENOTFOUND" || error.cause) {
      return { hasError: true, errorMessage: `ERR:CNT: ${error.message} : ${link}` };
    }
    return { hasError: true, errorMessage: `ERR:UKN: ${error.message} : ${link}` };
  } finally {
    clearTimeout(timeout);
  }
}

// Runs link checks with bounded concurrency (upstream ran fully sequential;
// a small worker pool keeps this tractable without hammering any one host).
async function checkLinksWorking(links, { concurrency = 10, timeoutMs = 25000 } = {}) {
  const errors = [];
  let index = 0;

  async function worker() {
    while (index < links.length) {
      const link = links[index++];
      const { hasError, errorMessage } = await checkIfLinkIsWorking(link, { timeoutMs });
      if (hasError) errors.push(errorMessage);
    }
  }

  const workers = Array.from({ length: Math.min(concurrency, links.length) }, worker);
  await Promise.all(workers);
  return errors;
}

module.exports = {
  findLinksInText,
  findLinksInFile,
  checkDuplicateLinks,
  getHostFromLink,
  hasCloudflareProtection,
  checkIfLinkIsWorking,
  checkLinksWorking,
  fakeUserAgent,
};

import type { ApiType } from "@repo/shared";
import React from "react";

const authLabel = (auth: ApiType["auth"]) => {
  switch (auth) {
    case "apiKey":
      return "API Key";
    case "No":
      return "None";
    case "OAuth":
      return "OAuth";
    case "X-Mashape-Key":
      return "X-Mashape-Key";
    case "User-Agent":
      return "User-Agent";
    default:
      return String(auth);
  }
};

const corsLabel = (cors: ApiType["cors"]) => {
  switch (cors) {
    case "Yes":
      return "Yes";
    case "No":
      return "No";
    case "Unknown":
      return "Unknown";
    default:
      return String(cors);
  }
};

const ApiDisplay = ({
  api,
  status,
  checking,
  onCheckStatus,
}: {
  api: ApiType;
  status: { status: ApiType["status"] | null } | null;
  checking: boolean;
  onCheckStatus: (link: string) => void;
}) => {
  return (
    <div className="flex h-full flex-col gap-3 rounded-2xl border border-zinc-200 bg-white p-5 shadow-sm transition hover:-translate-y-1 hover:shadow-lg dark:border-zinc-800 dark:bg-zinc-900">
      <div className="flex items-start justify-between gap-2">
        <div>
          <h3 className="text-lg font-semibold">{api.name}</h3>
          <p className="text-sm text-zinc-500">{api.category}</p>
        </div>
        {api.link && status ? (
          <span
            className={`rounded-full px-2 py-1 text-xs ${status?.status === "online" ? "text-emerald-700 bg-emerald-100" : status?.status === "offline" ? "text-rose-700 bg-rose-100" : "text-zinc-700 bg-zinc-100"}`}
          >
            Status: {status && (checking ? "checking" : status?.status)}
          </span>
        ) : (
          <button
            type="button"
            onClick={() => onCheckStatus(api.link)}
            disabled={checking}
            className="rounded-full border border-zinc-300 px-3 py-1 text-xs font-semibold text-zinc-600 dark:text-zinc-300 dark:hover:text-zinc-100 transition hover:border-zinc-400 hover:text-zinc-900 disabled:cursor-not-allowed disabled:opacity-60 cursor-pointer"
          >
            {checking ? "Checking..." : "Check status"}
          </button>
        )}
        {/* {api.link && (
          <span className="rounded-full bg-zinc-100 px-2 py-1 text-zinc-700">
            Status:{" "}
            {status ? (
              checking ? (
                "checking"
              ) : (
                "not checked"
              )
            ) : (
              <button
                type="button"
                onClick={() => onCheckStatus(api.link)}
                disabled={checking}
                className="rounded-full border border-zinc-300 px-3 py-1 text-xs font-semibold text-zinc-600 transition hover:border-zinc-400 hover:text-zinc-900 disabled:cursor-not-allowed disabled:opacity-60"
              >
                {checking ? "Checking..." : "Check status"}
              </button>
            )}
          </span>
        )} */}
      </div>

      <p className="text-sm text-zinc-600">{api.description}</p>

      <div className="mt-auto flex flex-wrap gap-2 text-xs">
        <span className="rounded-full bg-blue-100 px-2 py-1 text-blue-700">
          {authLabel(api.auth)}
        </span>
        <span className="rounded-full bg-purple-100 px-2 py-1 text-purple-700">
          CORS: {corsLabel(api.cors)}
        </span>
        <span
          className={`rounded-full px-2 py-1 text-xs font-semibold ${
            api.https
              ? "bg-emerald-100 text-emerald-700"
              : "bg-rose-100 text-rose-700"
          }`}
        >
          {api.https ? "HTTPS" : "HTTP"}
        </span>
      </div>

      {api.link ? (
        <div className="mt-2 flex items-center gap-3">
          <a
            href={api.link}
            target="_blank"
            rel="noreferrer"
            className="text-sm font-semibold text-blue-700 hover:text-blue-600"
          >
            Go to documentation
          </a>
        </div>
      ) : (
        <span className="mt-2 text-sm font-semibold text-zinc-400">
          No documentation link
        </span>
      )}
    </div>
  );
};

export default ApiDisplay;

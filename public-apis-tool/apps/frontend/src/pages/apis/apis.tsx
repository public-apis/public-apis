import React, { useEffect, useMemo, useState } from "react";
import type { ApiType } from "@repo/shared";
import { apiClient } from "../../api/api-client";
import { APIS_ROUTE } from "../../utils/constants";

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

const ApisPage = () => {
  const [apis, setApis] = useState<ApiType[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [query, setQuery] = useState("");
  const [selectedCategories, setSelectedCategories] = useState<string[]>([]);
  const [selectedAuth, setSelectedAuth] = useState<ApiType["auth"][]>([]);
  const [httpsOnly, setHttpsOnly] = useState<"all" | "yes" | "no">("all");
  const [selectedCors, setSelectedCors] = useState<ApiType["cors"][]>([]);

  useEffect(() => {
    let active = true;
    setLoading(true);
    setError(null);
    apiClient
      .get<ApiType[]>(APIS_ROUTE)
      .then((res) => {
        if (!active) return;
        setApis(res.data ?? []);
      })
      .catch((err) => {
        if (!active) return;
        setError(err?.message ?? "Failed to load APIs");
        setApis([]);
      })
      .finally(() => {
        if (!active) return;
        setLoading(false);
      });

    return () => {
      active = false;
    };
  }, []);

  const categories = useMemo(
    () => Array.from(new Set(apis.map((api) => api.category))).sort(),
    [apis]
  );

  const authTypes = useMemo(
    () => Array.from(new Set(apis.map((api) => api.auth))).sort(),
    [apis]
  );

  const corsOptions = useMemo(
    () => Array.from(new Set(apis.map((api) => api.cors))).sort(),
    [apis]
  );

  const filteredApis = useMemo(() => {
    const normalizedQuery = query.trim().toLowerCase();
    return apis.filter((api) => {
      const matchesQuery =
        normalizedQuery.length === 0 ||
        api.name.toLowerCase().includes(normalizedQuery) ||
        api.description.toLowerCase().includes(normalizedQuery) ||
        api.category.toLowerCase().includes(normalizedQuery);

      const matchesCategory =
        selectedCategories.length === 0 ||
        selectedCategories.includes(api.category);

      const matchesAuth =
        selectedAuth.length === 0 || selectedAuth.includes(api.auth);

      const matchesHttps =
        httpsOnly === "all" ||
        (httpsOnly === "yes" && api.https) ||
        (httpsOnly === "no" && !api.https);

      const matchesCors =
        selectedCors.length === 0 || selectedCors.includes(api.cors);

      return (
        matchesQuery &&
        matchesCategory &&
        matchesAuth &&
        matchesHttps &&
        matchesCors
      );
    });
  }, [apis, query, selectedCategories, selectedAuth, httpsOnly, selectedCors]);

  const toggleValue = <T,>(value: T, list: T[], setList: (v: T[]) => void) => {
    if (list.includes(value)) {
      setList(list.filter((item) => item !== value));
      return;
    }
    setList([...list, value]);
  };

  const clearFilters = () => {
    setQuery("");
    setSelectedCategories([]);
    setSelectedAuth([]);
    setHttpsOnly("all");
    setSelectedCors([]);
  };

  return (
    <div className="flex w-full justify-center px-4 py-8">
      <div className="flex w-full max-w-342 flex-col gap-6">
        <div className="flex flex-col gap-2">
          <h1 className="text-3xl font-semibold tracking-widest">APIs</h1>
          <p className="text-zinc-500">
            Intuitive search and filtering. Combine multiple filters
            at once.
          </p>
        </div>

        <div className="grid gap-6 rounded-2xl border border-zinc-200 bg-white p-6 shadow-sm dark:border-zinc-800 dark:bg-zinc-900">
          <div className="flex flex-col gap-3">
            <label className="text-sm font-medium text-zinc-500">
              Search by name or keywords
            </label>
            <input
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              placeholder="For example. weather, crypto, github"
              className="w-full rounded-xl border border-zinc-200 bg-white px-4 py-2 text-sm focus:border-blue-500 focus:outline-none dark:border-zinc-700 dark:bg-zinc-950"
            />
          </div>

          <div className="grid gap-6 lg:grid-cols-3">
            <div className="flex flex-col gap-3">
              <p className="text-sm font-semibold text-zinc-500">Categories</p>
              <div className="flex flex-wrap gap-2">
                {categories.map((category) => (
                  <button
                    key={category}
                    onClick={() =>
                      toggleValue(category, selectedCategories, setSelectedCategories)
                    }
                    className={`rounded-full border px-3 py-1 text-xs font-medium transition ${
                      selectedCategories.includes(category)
                        ? "border-blue-600 bg-blue-600 text-white"
                        : "border-zinc-300 bg-white text-zinc-700 hover:border-blue-400 dark:border-zinc-700 dark:bg-zinc-950 dark:text-zinc-200"
                    }`}
                  >
                    {category}
                  </button>
                ))}
              </div>
            </div>

            <div className="flex flex-col gap-3">
              <p className="text-sm font-semibold text-zinc-500">Auth</p>
              <div className="flex flex-wrap gap-2">
                {authTypes.map((auth) => (
                  <button
                    key={auth}
                    onClick={() =>
                      toggleValue(auth, selectedAuth, setSelectedAuth)
                    }
                    className={`rounded-full border px-3 py-1 text-xs font-medium transition ${
                      selectedAuth.includes(auth)
                        ? "border-emerald-600 bg-emerald-600 text-white"
                        : "border-zinc-300 bg-white text-zinc-700 hover:border-emerald-400 dark:border-zinc-700 dark:bg-zinc-950 dark:text-zinc-200"
                    }`}
                  >
                    {authLabel(auth)}
                  </button>
                ))}
              </div>
            </div>

            <div className="flex flex-col gap-3">
              <p className="text-sm font-semibold text-zinc-500">CORS</p>
              <div className="flex flex-wrap gap-2">
                {corsOptions.map((cors) => (
                  <button
                    key={cors}
                    onClick={() =>
                      toggleValue(cors, selectedCors, setSelectedCors)
                    }
                    className={`rounded-full border px-3 py-1 text-xs font-medium transition ${
                      selectedCors.includes(cors)
                        ? "border-purple-600 bg-purple-600 text-white"
                        : "border-zinc-300 bg-white text-zinc-700 hover:border-purple-400 dark:border-zinc-700 dark:bg-zinc-950 dark:text-zinc-200"
                    }`}
                  >
                    {corsLabel(cors)}
                  </button>
                ))}
              </div>
            </div>
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <p className="text-sm font-semibold text-zinc-500">HTTPS</p>
            <div className="flex items-center gap-2">
              {[
                { value: "all", label: "All" },
                { value: "yes", label: "HTTPS only" },
                { value: "no", label: "No HTTPS" },
              ].map((option) => (
                <button
                  key={option.value}
                  onClick={() => setHttpsOnly(option.value as "all" | "yes" | "no")}
                  className={`rounded-full border px-3 py-1 text-xs font-medium transition ${
                    httpsOnly === option.value
                      ? "border-blue-700 bg-blue-700 text-white"
                      : "border-zinc-300 bg-white text-zinc-700 hover:border-blue-400 dark:border-zinc-700 dark:bg-zinc-950 dark:text-zinc-200"
                  }`}
                >
                  {option.label}
                </button>
              ))}
            </div>

            <button
              onClick={clearFilters}
              className="ml-auto rounded-full border border-zinc-300 px-4 py-1 text-xs font-semibold text-zinc-600 transition hover:border-zinc-400 hover:text-zinc-900 dark:border-zinc-700 dark:text-zinc-300"
            >
              Clear filters
            </button>
          </div>
        </div>

        <div className="flex items-center justify-between text-sm text-zinc-500">
          <p>
            Found <span className="font-semibold">{filteredApis.length}</span>{" "}
            out of <span className="font-semibold">{apis.length}</span>
          </p>
          <p>Shown based on selected filters</p>
        </div>

        {loading && (
          <div className="rounded-2xl border border-dashed border-zinc-300 p-8 text-center text-zinc-500">
            Loading APIs...
          </div>
        )}

        {error && !loading && (
          <div className="rounded-2xl border border-dashed border-rose-300 p-8 text-center text-rose-600">
            {error}
          </div>
        )}

        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {filteredApis.map((api, index) => (
            <div
              key={`${api.name}-${api.category}-${api.link ?? "no-link"}-${index}`}
              className="flex h-full flex-col gap-3 rounded-2xl border border-zinc-200 bg-white p-5 shadow-sm transition hover:-translate-y-1 hover:shadow-lg dark:border-zinc-800 dark:bg-zinc-900"
            >
              <div className="flex items-start justify-between gap-2">
                <div>
                  <h3 className="text-lg font-semibold">{api.name}</h3>
                  <p className="text-sm text-zinc-500">{api.category}</p>
                </div>
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

              <p className="text-sm text-zinc-600">{api.description}</p>

              <div className="mt-auto flex flex-wrap gap-2 text-xs">
                <span className="rounded-full bg-blue-100 px-2 py-1 text-blue-700">
                  {authLabel(api.auth)}
                </span>
                <span className="rounded-full bg-purple-100 px-2 py-1 text-purple-700">
                  CORS: {corsLabel(api.cors)}
                </span>
              </div>

              {api.link ? (
                <a
                  href={api.link}
                  target="_blank"
                  rel="noreferrer"
                  className="mt-2 text-sm font-semibold text-blue-700 hover:text-blue-600"
                >
                  Go to documentation
                </a>
              ) : (
                <span className="mt-2 text-sm font-semibold text-zinc-400">
                  No documentation link
                </span>
              )}
            </div>
          ))}
        </div>

        {filteredApis.length === 0 && !loading && !error && (
          <div className="rounded-2xl border border-dashed border-zinc-300 p-8 text-center text-zinc-500">
           Nothing found. Please change your search query or filters.
          </div>
        )}
      </div>
    </div>
  );
};

export default ApisPage;

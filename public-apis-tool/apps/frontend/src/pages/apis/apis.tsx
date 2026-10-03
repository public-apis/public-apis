import React, { useEffect, useMemo, useState } from "react";
import type { ApiType } from "@repo/shared";
import { apiClient } from "../../api/api-client";
import { APIS_ROUTE } from "../../utils/constants";
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible";
import { ChevronDown, ChevronUp, Filter, FilterX } from "lucide-react";
import ApiDisplay from "./components/api-display";
import { BeatLoader } from "react-spinners";
import ApiPages from "./components/api-pages";

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
  const [filtersOpen, setFiltersOpen] = useState(true);
  const [apis, setApis] = useState<ApiType[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [statusByLink, setStatusByLink] = useState<
    Record<string, { status: ApiType["status"] | null } | null>
  >({});
  const [checkingByLink, setCheckingByLink] = useState<Record<string, boolean>>(
    {},
  );
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
    [apis],
  );

  const authTypes = useMemo(
    () => Array.from(new Set(apis.map((api) => api.auth))).sort(),
    [apis],
  );

  const corsOptions = useMemo(
    () => Array.from(new Set(apis.map((api) => api.cors))).sort(),
    [apis],
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

  const handleCheckStatus = async (link: string) => {
    if (!link) return;

    setCheckingByLink((prev) => ({ ...prev, [link]: true }));

    try {
      const res = await apiClient.get<{ status: ApiType["status"] | null }>(
        `${APIS_ROUTE}/check`,
        {
          params: { url: link },
        },
      );

      setStatusByLink((prev) => ({ ...prev, [link]: res.data ?? null }));
    } catch {
      setStatusByLink((prev) => ({ ...prev, [link]: null }));
    } finally {
      setCheckingByLink((prev) => ({ ...prev, [link]: false }));
    }
  };

  return (
    <div className="flex w-full justify-center px-4 py-8">
      <div className="flex w-full max-w-342 flex-col gap-6">
        <div className="flex flex-col gap-2">
          <h1 className="text-3xl font-semibold tracking-widest">APIs</h1>
          <p className="text-zinc-500">
            Intuitive search and filtering. Combine multiple filters at once.
          </p>
        </div>

        <Collapsible
          open={filtersOpen}
          onOpenChange={setFiltersOpen}
          className="grid gap-6 rounded-2xl border border-zinc-200 bg-white p-6 shadow-sm dark:border-zinc-800 dark:bg-zinc-900"
        >
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

          <CollapsibleTrigger className="flex justify-between items-center p-2 rounded-xl hover:bg-zinc-100/50 dark:hover:bg-zinc-800/50 cursor-pointer transition-all duration-300">
            <p className="text-lg">Filters</p>
            <div className="flex gap-1">
              <Filter size={22} />
              {filtersOpen ? (
                <ChevronUp size={22} />
              ) : (
                <ChevronDown size={22} />
              )}
            </div>
          </CollapsibleTrigger>
          <CollapsibleContent className="grid gap-6">
            <div>
              <div className="flex flex-col gap-3">
                <p className="text-sm font-semibold text-zinc-500">
                  Categories
                </p>
                <div className="flex flex-wrap gap-2">
                  {categories.map((category) => (
                    <button
                      key={category}
                      onClick={() =>
                        toggleValue(
                          category,
                          selectedCategories,
                          setSelectedCategories,
                        )
                      }
                      className={`rounded-full border px-3 py-1 text-xs font-medium transition cursor-pointer ${
                        selectedCategories.includes(category)
                          ? "border-blue-600 bg-blue-600 text-white"
                          : "border-zinc-300 bg-white text-zinc-700 hover:border-blue-400 dark:border-zinc-700 dark:bg-zinc-950 dark:text-zinc-200 dark:hover:border-blue-400"
                      }`}
                    >
                      {category}
                    </button>
                  ))}
                </div>
              </div>
            </div>
            <div className="grid gap-6 md:grid-cols-3">
              <div className="flex flex-col gap-3">
                <p className="text-sm font-semibold text-zinc-500">Auth</p>
                <div className="flex flex-wrap gap-2">
                  {authTypes.map((auth) => (
                    <button
                      key={auth}
                      onClick={() =>
                        toggleValue(auth, selectedAuth, setSelectedAuth)
                      }
                      className={`rounded-full border px-3 py-1 text-xs font-medium transition cursor-pointer ${
                        selectedAuth.includes(auth)
                          ? "border-emerald-600 bg-emerald-600 text-white"
                          : "border-zinc-300 bg-white text-zinc-700 hover:border-emerald-400 dark:border-zinc-700 dark:bg-zinc-950 dark:text-zinc-200 dark:hover:border-emerald-400"
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
                      className={`rounded-full border px-3 py-1 text-xs font-medium transition cursor-pointer ${
                        selectedCors.includes(cors)
                          ? "border-purple-600 bg-purple-600 text-white"
                          : "border-zinc-300 bg-white text-zinc-700 hover:border-purple-400 dark:border-zinc-700 dark:bg-zinc-950 dark:text-zinc-200 dark:hover:border-purple-400"
                      }`}
                    >
                      {corsLabel(cors)}
                    </button>
                  ))}
                </div>
              </div>
              <div className="flex flex-col gap-3">
                <p className="text-sm font-semibold text-zinc-500">HTTPS</p>
                <div className="flex flex-wrap gap-2">
                  {[
                    { value: "all", label: "All" },
                    { value: "yes", label: "HTTPS only" },
                    { value: "no", label: "No HTTPS" },
                  ].map((option) => (
                    <button
                      key={option.value}
                      onClick={() =>
                        setHttpsOnly(option.value as "all" | "yes" | "no")
                      }
                      className={`rounded-full border px-3 py-1 text-xs font-medium transition cursor-pointer ${
                        httpsOnly === option.value
                          ? "border-blue-700 bg-blue-700 text-white"
                          : "border-zinc-300 bg-white text-zinc-700 hover:border-blue-400 dark:border-zinc-700 dark:bg-zinc-950 dark:text-zinc-200 dark:hover:border-blue-400"
                      }`}
                    >
                      {option.label}
                    </button>
                  ))}
                </div>
              </div>
            </div>
            <div className="flex w-full justify-end">
              <button
                onClick={clearFilters}
                className="flex gap-2 rounded-full border border-zinc-300 px-4 py-1 text-sm font-semibold text-zinc-600 transition cursor-pointer hover:border-zinc-400 hover:text-zinc-900 dark:border-zinc-700 dark:text-zinc-300 dark:hover:border-zinc-400"
              >
                Clear filters
                <FilterX size={16} />
              </button>
            </div>
          </CollapsibleContent>
        </Collapsible>

        <div className="flex items-center justify-between text-sm text-zinc-500">
          <p>
            Found <span className="font-semibold">{filteredApis.length}</span>{" "}
            out of <span className="font-semibold">{apis.length}</span>
          </p>
          <p>Shown based on selected filters</p>
        </div>

        {loading && (
          <div className="flex justify-center rounded-2xl border border-dashed border-zinc-300 p-8 text-zinc-500">
            <BeatLoader color="#1d4ed8" size={18} />
          </div>
        )}

        {error && !loading && (
          <div className="rounded-2xl border border-dashed border-rose-300 p-8 text-center text-rose-600">
            {error}
          </div>
        )}

        {/* <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {filteredApis.map((api, index) => (
            <ApiDisplay
              key={`${api.name}-${api.category}-${api.link ?? "no-link"}-${index}`}
              api={api}
            />
          ))}
        </div> */}
        {filteredApis.length > 0 && (
          <ApiPages
            apis={filteredApis}
            statusByLink={statusByLink}
            checkingByLink={checkingByLink}
            onCheckStatus={handleCheckStatus}
          />
        )}

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

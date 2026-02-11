import React, { useEffect, useState } from "react";
import ApiDisplay from "./api-display";
import type { ApiType } from "@repo/shared";
import {
  ChevronLeft,
  ChevronRight,
  ChevronsLeft,
  ChevronsRight,
} from "lucide-react";

const ApiPages = ({ apis }: { apis: ApiType[] }) => {
  const total = Math.ceil(apis.length / 15);
  const [currentPage, setCurrentPage] = useState(1);
  const [selectedApis, setSelectedApis] = useState<ApiType[]>([]);
  const [pagesToDisplay, setPagesToDisplay] = useState<number[]>([]);

  const getPaginationPages = () => {
    if (total <= 3) {
      return Array.from({ length: total }, (_, i) => i + 1);
    }

    if (currentPage === 1) return [1, 2, 3];
    if (currentPage === total) return [total - 2, total - 1, total];

    return [currentPage - 1, currentPage, currentPage + 1];
  };

  useEffect(() => {
    const apisToDisplay = [...apis].slice(
      (currentPage - 1) * 15,
      currentPage * 15,
    );
    setSelectedApis(apisToDisplay);
    setPagesToDisplay(getPaginationPages());
  }, [currentPage, apis, total]);

  useEffect(() => {
    setCurrentPage(1);
    setPagesToDisplay(getPaginationPages());
  }, [apis, total]);

  return (
    <>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {selectedApis.map((api, index) => (
          <ApiDisplay
            key={`${api.name}-${api.category}-${api.link ?? "no-link"}-${index}`}
            api={api}
          />
        ))}
      </div>

      <div className="flex gap-8 justify-center">
        <div className="flex gap-2">
          <button
            disabled={currentPage === 1}
            onClick={() => {
              setCurrentPage(1);
            }}
            className="opacity-80 hover:opacity-90 disabled:opacity-40 disabled:cursor-auto transition cursor-pointer"
          >
            <ChevronsLeft />
          </button>
          <button
            disabled={currentPage === 1}
            onClick={() => {
              setCurrentPage(currentPage - 1);
            }}
            className="opacity-80 hover:opacity-90 disabled:opacity-40 disabled:cursor-auto transition cursor-pointer"
          >
            <ChevronLeft />
          </button>
        </div>

        <div className="flex gap-2">
          {pagesToDisplay.map((p) => (
            <button
              key={p}
              onClick={() => {
                setCurrentPage(p);
              }}
              className={`border w-8 h-8 rounded-lg cursor-pointer hover:border-blue-400 transition ${currentPage === p && "text-zinc-100 bg-blue-700"}`}
            >
              {p}
            </button>
          ))}
        </div>

        <div className="flex gap-2">
          <button
            disabled={currentPage === total}
            onClick={() => {
              setCurrentPage(currentPage + 1);
            }}
            className="opacity-80 hover:opacity-90 disabled:opacity-40 disabled:cursor-auto transition cursor-pointer"
          >
            <ChevronRight />
          </button>
          <button
            disabled={currentPage === total}
            onClick={() => {
              setCurrentPage(total);
            }}
            className="opacity-80 hover:opacity-90 disabled:opacity-40 disabled:cursor-auto transition cursor-pointer"
          >
            <ChevronsRight />
          </button>
        </div>
      </div>
      <div className="text-center text-sm opacity-50">
        Page {currentPage}/{total}
      </div>
    </>
  );
};

export default ApiPages;

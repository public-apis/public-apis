import { apiClient } from "@/api/api-client";
import { PR_HISTORY_ROUTE } from "@/utils/constants";
import React, { useEffect, useState } from "react";
import PRDisplay from "./pr-display";
import { Skeleton } from "@/components/ui/skeleton";

const PRHistory = () => {
  const [loading, setLoading] = useState(true);
  const [prs, setPrs] = useState([]);

  const getPRs = async () => {
    await apiClient
      .get(PR_HISTORY_ROUTE, { withCredentials: true })
      .then((res) => {
        console.log(res.data.prs);
        setPrs(res.data.prs);
      })
      .catch((err) => {
        console.error(err);
        setPrs([]);
      })
      .finally(() => {
        setLoading(false);
      });
  };

  useEffect(() => {
    getPRs();
  }, []);

  if (loading)
    return (
      <div className="flex w-full items-center justify-center px-2">
        {/* <BeatLoader color="#1d4ed8" size={18} /> */}
        <div className="flex flex-col w-full gap-3 max-w-132">
          {Array.from({ length: 3 }).map((_, i) => (
            <div className="flex flex-col gap-3 w-full bg-zinc-100 dark:bg-zinc-800 p-3 rounded-lg">
              <Skeleton className="w-1/3 h-4 bg-zinc-200 dark:bg-zinc-700" />
              <Skeleton className="w-full h-6 bg-zinc-200 dark:bg-zinc-700" />
              <Skeleton className="w-1/4 h-4 bg-zinc-200 dark:bg-zinc-700" />
              <Skeleton className="w-4/9 h-4 bg-zinc-200 dark:bg-zinc-700 ml-auto" />
            </div>
          ))}
        </div>
      </div>
    );

  if (!prs || prs.length === 0)
    return (
      <div className="flex w-full items-center justify-center px-2">
        No Pull Requests found
      </div>
    );

  return (
    <div className="flex w-full items-center justify-center px-2">
      <div className="flex flex-col w-full gap-3 max-w-132">
        {prs.map((pr) => (
          <PRDisplay pr={pr} />
        ))}
      </div>
    </div>
  );
};

export default PRHistory;

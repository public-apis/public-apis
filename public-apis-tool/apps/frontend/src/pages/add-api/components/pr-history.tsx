import { apiClient } from "@/api/api-client";
import { PR_HISTORY_ROUTE } from "@/utils/constants";
import React, { useEffect, useState } from "react";
import { BeatLoader } from "react-spinners";
import PRDisplay from "./pr-display";

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
        <BeatLoader color="#1d4ed8" size={18} />
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

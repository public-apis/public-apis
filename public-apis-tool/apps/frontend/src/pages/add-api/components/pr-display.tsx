import dayjs from "dayjs";
import React from "react";

type prType = {
  number: number;
  title: string;
  user: string;
  state: string;
  merged: boolean;
  created_at: Date;
  updated_at: Date;
  url: string;
};

const PRDisplay = ({ pr }: { pr: prType }) => {
  return (
    <div className="flex flex-col gap-1 w-full bg-zinc-100 dark:bg-zinc-800 p-3 rounded-lg">
      <p className="opacity-60">Pull Request #{pr.number}</p>
      <a href={pr.url} className="text-lg">
        {pr.title}
      </a>
      <p>
        <span className="font-semibold">Status: </span>
        {pr.merged ? (
          <span className="text-emerald-600">Merged</span>
        ) : pr.state === "open" ? (
          <span className="text-yellow-600">Open</span>
        ) : (
          <span className="text-red-600">Closed</span>
        )}
      </p>
      <p className="text-sm opacity-60">
        Created at: {dayjs(pr.created_at).format("lll")}
      </p>
    </div>
  );
};

export default PRDisplay;

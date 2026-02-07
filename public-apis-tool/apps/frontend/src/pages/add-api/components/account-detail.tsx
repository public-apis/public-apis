import { useStore } from "@/store";
import { Github } from "lucide-react";
import React from "react";

const AccountDetail = () => {
  const { user } = useStore();
  if (!user) {
    return (
      <div className="flex w-full justify-center items-center h-[70vh]">
        <div className="flex flex-col w-full max-w-102 gap-4 items-center justify-center text-center">
          <p className="text-2xl font-semibold">Authorization required!</p>
          <p className="text-md opacity-90">
            You are not authorized with your github account. Use button below to
            login.
          </p>
          <button className="flex gap-2 justify-center items-center py-2 px-4 bg-zinc-900 dark:bg-zinc-100 shadow-zinc-900/30 dark:shadow-zinc-100/30 hover:shadow-lg rounded-lg cursor-pointer transition-shadow duration-300">
            <Github className="invert" />
            <p className="text-md font-semibold text-zinc-100 dark:text-zinc-900">
              Sign in with GitHub
            </p>
          </button>
        </div>
      </div>
    );
  }
  return <div>AccountDetail</div>;
};

export default AccountDetail;

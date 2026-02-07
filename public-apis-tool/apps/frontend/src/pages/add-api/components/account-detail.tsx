import { apiClient } from "@/api/api-client";
import { useStore } from "@/store";
import { GITHUB_AUTH_ROUTE, LOGOUT_ROUTE } from "@/utils/constants";
import { Github, LogOut } from "lucide-react";
import React from "react";
import { toast } from "sonner";

const AccountDetail = () => {
  const user = useStore((state) => state.user);
  const clearUser = useStore((state) => state.clearUser);

  const handleLogout = async () => {
    await apiClient.get(LOGOUT_ROUTE, { withCredentials: true }).then(() => {
      clearUser();
      toast.success("Logged out successfully");
    });
  };

  if (!user) {
    return (
      <div className="flex w-full justify-center items-center h-[70vh] px-2">
        <div className="flex flex-col w-full max-w-102 gap-4 items-center justify-center text-center">
          <p className="text-2xl font-semibold">Authorization required!</p>
          <img
            src="./tech-icons/github.png"
            alt="GitHub"
            className="w-[50vw] max-w-48"
          />
          <p className="text-md opacity-90">
            You are not authorized with your github account. Use button below to
            login.
          </p>
          <a
            href={GITHUB_AUTH_ROUTE}
            className="flex gap-2 justify-center items-center py-2 px-4 bg-zinc-900 dark:bg-zinc-100 shadow-zinc-900/30 dark:shadow-zinc-100/30 hover:shadow-lg rounded-lg cursor-pointer transition-shadow duration-300"
          >
            <Github className="invert" />
            <p className="text-md font-semibold text-zinc-100 dark:text-zinc-900">
              Sign in with GitHub
            </p>
          </a>
        </div>
      </div>
    );
  }
  return (
    <div className="flex w-full justify-center items-center py-4">
      <div className="flex flex-col w-full gap-4 items-center justify-center text-center">
        <div className="h-32 w-32 rounded-full">
          <img src={user.avatar} alt="" className="rounded-full" />
        </div>
        <p className="text-xl font-semibold">Hello, {user.login}!</p>
        <button
          className="flex gap-2 justify-center items-center py-2 px-4 bg-zinc-900 dark:bg-zinc-100 shadow-zinc-900/30 dark:shadow-zinc-100/30 hover:shadow-lg rounded-lg cursor-pointer transition-shadow duration-300"
          onClick={handleLogout}
        >
          <LogOut className="invert" />
          <p className="text-md font-semibold text-zinc-100 dark:text-zinc-900">
            Log Out
          </p>
        </button>
      </div>
    </div>
  );
};

export default AccountDetail;

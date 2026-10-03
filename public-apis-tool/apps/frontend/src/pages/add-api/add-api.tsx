import React from "react";
import AccountDetail from "./components/account-detail";
import { useStore } from "@/store";
import PRTabs from "./components/pr-tabs";

const AddApi = () => {
  const user = useStore((state) => state.user);
  return (
    <div className="flex flex-col w-full max-w-342 py-4">
      <p className="text-center text-3xl font-semibold tracking-widest">
        Add API
      </p>
      <AccountDetail />
      {user && <PRTabs />}
    </div>
  );
};

export default AddApi;

import React from "react";
import AccountDetail from "./components/account-detail";

const AddApi = () => {
  return (
    <div className="flex flex-col w-full max-w-342 py-4">
      <p className="text-center text-3xl font-semibold tracking-widest">
        Add API
      </p>
      <AccountDetail />
    </div>
  );
};

export default AddApi;

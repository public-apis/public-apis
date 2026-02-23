import React from "react";
import Header from "./components/header";
import { Outlet } from "react-router-dom";
import Footer from "./components/footer";

const Layout = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <div className="flex w-full justify-center">
        <Outlet />
      </div>
      <Footer />
    </div>
  );
};

export default Layout;

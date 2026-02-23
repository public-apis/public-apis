import ThemeToggler from "@/components/theme-toggler.tsx";
import React from "react";
import { Link, NavLink } from "react-router-dom";

const Header = () => {
  return (
    <header>
      <div className="flex w-full p-4 justify-center bg-zinc-100 dark:bg-zinc-900 shadow-xl">
        <div className="flex w-full max-w-342 justify-between items-center">
          <div>
            <Link to={"/"} className="flex gap-4 items-center">
              <img src="/api-logo.png" alt="Logo" width={"36px"} />
              <p className="text-xl font-light">Public APIs</p>
            </Link>
          </div>
          <div className="flex items-center gap-6">
            <NavLink
              to="/apis"
              className={({ isActive }) =>
                `flex items-center gap-4 opacity-90 hover:opacity-100 ${isActive && "text-blue-600"}`
              }
            >
              APIs List
            </NavLink>
            <NavLink
              to="/add-api"
              className={({ isActive }) =>
                `flex items-center gap-4 ${isActive && "text-blue-600"}`
              }
            >
              Add API
            </NavLink>

            <ThemeToggler />
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;

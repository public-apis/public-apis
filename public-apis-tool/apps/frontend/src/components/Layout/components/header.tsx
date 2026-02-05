import ThemeToggler from "@/components/theme-toggler.tsx";
import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <header>
      <div className="flex w-full p-4 justify-center bg-zinc-100 dark:bg-zinc-900 shadow-xl">
        <div className="flex w-full max-w-342 justify-between items-center">
          <div>
            <Link to={"/"}>
              <img src="/api-logo.png" alt="Logo" width={"48px"} />
            </Link>
          </div>
          <div className="flex items-center gap-4">
            <p>Link1</p>
            <p>Link2</p>
            <ThemeToggler />
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;

import React from "react";
import { Sun, Moon } from "lucide-react";
import { useTheme } from "@/context/themeContext";

const ThemeToggler = () => {
  const { theme, toggleTheme } = useTheme();
  return (
    <button
      onClick={toggleTheme}
      className="p-2 rounded-full bg-black/10 dark:bg-white/10 cursor-pointer transition-all duration-300"
    >
      {theme === "dark" ? <Sun /> : <Moon />}
    </button>
  );
};

export default ThemeToggler;

import React from "react";

const Footer = () => {
  return (
    <div className="flex justify-center mt-auto p-4 border-t bg-zinc-100 dark:bg-zinc-900 inset-shadow-xl">
      <div className="flex max-w-342 w-full flex-col xl:flex-row items-center justify-center xl:justify-between text-zinc-500">
        <p>Public APIs tool</p>
        <p>Altunyan Arsen, Oleksandr Ivanov</p>
        <p>FIT KNU, IPZ-33/6</p>
      </div>
    </div>
  );
};

export default Footer;

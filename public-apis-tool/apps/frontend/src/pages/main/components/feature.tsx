import React from "react";

interface FeatureProps {
  children: React.ReactNode;
  title: string;
  image: string;
}

const Feature = ({ children, title, image }: FeatureProps) => {
  return (
    <div className="w-full rounded-xl bg-linear-to-br dark:from-zinc-800 to-zinc-200 dark:to-zinc-900 shadow-md p-4">
      <div className="flex justify-between items-center">
        <div className="flex-1 flex flex-col items-center text-center">
          <p className="font-semibold text-2xl text-center">{title}</p>
          <p className="text-lg opacity-75">{children}</p>
        </div>
        <img src={image} alt="FeatureIcon" className="w-24" />
      </div>
    </div>
  );
};

export default Feature;

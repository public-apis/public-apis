import React from "react";
import { motion } from "framer-motion";

const Main = () => {
  return (
    <div className="flex w-full justify-center py-4">
      <div className="flex flex-col w-full max-w-342 h-[90vh] justify-center items-center gap-4">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          <img src="/api-logo.png" alt="Logo" className="w-[60vw] max-w-48" />
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.5, delay: 0.1 }}
        >
          <p className="text-3xl font-bold tracking-widest">Public APIs tool</p>
        </motion.div>
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.5, delay: 0.2 }}
        >
          <p className="text-xl opacity-75">
            Explore free public APIs and share your own ones
          </p>
        </motion.div>
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.3 }}
        >
          <button className="cursor-pointer text-zinc-100 rounded-xl bg-blue-700 hover:bg-blue-600 hover:shadow-md hover:shadow-blue-600/50 px-12 py-2 text-lg transition-all duration-300">
            View APIs
          </button>
        </motion.div>
      </div>
    </div>
  );
};

export default Main;

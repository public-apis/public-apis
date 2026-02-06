import React from "react";
import { motion } from "framer-motion";
import Feature from "./components/feature";
import TechCard from "./components/tech-card";

const Main = () => {
  return (
    <div className="flex flex-col w-full justify-center items-center py-4">
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
      <div className="py-6 w-full max-w-342">
        <p className="font-semibold tracking-widest text-3xl text-center">
          Features
        </p>
        <div className="grid my-12 grid-cols-1 md:grid-cols-2 gap-12 px-4">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.4 }}
            viewport={{ once: true }}
          >
            <Feature title="Search APIs" image="/search.png">
              Find the necessary API by name or keywords
            </Feature>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.4, delay: 0.1 }}
            viewport={{ once: true }}
          >
            <Feature title="Filtering" image="/filter.png">
              Filter APIs by category, HTTPS support, and auth type
            </Feature>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.4, delay: 0.2 }}
            viewport={{ once: true }}
          >
            <Feature title="API Status" image="/status.png">
              Check if the API is still working and up-to-date
            </Feature>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.4, delay: 0.3 }}
            viewport={{ once: true }}
          >
            <Feature title="Pull Request" image="/pull-request.png">
              Create a pull request to add your own API to the list
            </Feature>
          </motion.div>
        </div>
      </div>

      <div className="py-6 w-full max-w-342">
        <p className="font-semibold tracking-widest text-3xl text-center">
          Tech Stack
        </p>
        <div className="flex w-full items-center justify-center gap-12 px-4 my-12">
          <TechCard
            name="React"
            logo="./tech-icons/react.png"
            gradient="bg-gradient-to-br from-cyan-500 to-blue-600"
          />
          <TechCard
            name="TypeScript"
            logo="./tech-icons/typescript.png"
            gradient="bg-gradient-to-br from-blue-400 to-indigo-600"
          />
          <TechCard
            name="Tailwind CSS"
            logo="./tech-icons/tailwind.png"
            gradient="bg-gradient-to-br from-cyan-600 to-blue-700"
          />
          <TechCard
            name="Zustand"
            logo="./tech-icons/zustand.png"
            gradient="bg-gradient-to-br from-yellow-400 to-yellow-600"
          />

          <TechCard
            name="Node.js"
            logo="./tech-icons/nodejs.png"
            gradient="bg-gradient-to-br from-green-500 to-emerald-700"
          />

          <TechCard
            name="NestJS"
            logo="./tech-icons/nestjs.png"
            gradient="bg-gradient-to-br from-red-500 to-rose-700"
          />

          <TechCard
            name="GitHub"
            logo="./tech-icons/github.png"
            gradient="bg-gradient-to-br from-gray-700 to-black"
          />
        </div>
      </div>
    </div>
  );
};

export default Main;

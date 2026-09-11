import { motion } from "framer-motion";

interface TechCardProps {
  name: string;
  logo: string;
  gradient: string; // tailwind gradient classes
  animationDelay: number;
}

const TechCard = ({ name, logo, gradient, animationDelay }: TechCardProps) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 100, y: 0 }}
      transition={{ duration: 0.4, delay: animationDelay }}
      viewport={{ once: true }}
    >
      <motion.div
        whileHover="hover"
        initial="rest"
        animate="rest"
        className={`relative overflow-hidden rounded-2xl p-6 shadow-md ${gradient} cursor-pointer flex items-center justify-center w-32 h-32`}
      >
        {/* Logo */}
        <motion.img
          src={logo}
          alt={name}
          className="w-16 h-16 object-contain"
          variants={{
            rest: { y: 0 },
            hover: { y: -18 },
          }}
          transition={{ duration: 0.3 }}
        />

        {/* Name */}
        <motion.div
          className="absolute bottom-5 text-white font-semibold text-lg"
          variants={{
            rest: { opacity: 0, y: 10 },
            hover: { opacity: 1, y: 0 },
          }}
          transition={{ duration: 0.3 }}
        >
          {name}
        </motion.div>
      </motion.div>
    </motion.div>
  );
};

export default TechCard;

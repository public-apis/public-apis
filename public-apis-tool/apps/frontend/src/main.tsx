import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.tsx";
import { ThemeProvider } from "./context/themeContext.tsx";
import { Toaster } from "./components/ui/sonner.tsx";

import dayjs from "dayjs";
import localizedFormat from "dayjs/plugin/localizedFormat";
import relativeTime from "dayjs/plugin/relativeTime";
import "dayjs/locale/uk";

dayjs.extend(localizedFormat);
dayjs.extend(relativeTime);
dayjs.locale("uk");

createRoot(document.getElementById("root")!).render(
  // <StrictMode>
  <ThemeProvider>
    <App />
    <Toaster position="top-center" />
  </ThemeProvider>,
  // </StrictMode>,
);

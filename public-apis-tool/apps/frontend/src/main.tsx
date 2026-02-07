import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.tsx";
import { ThemeProvider } from "./context/themeContext.tsx";
import { Toaster } from "./components/ui/sonner.tsx";

createRoot(document.getElementById("root")!).render(
  // <StrictMode>
  <ThemeProvider>
    <App />
    <Toaster />
  </ThemeProvider>,
  // </StrictMode>,
);

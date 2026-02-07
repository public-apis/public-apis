import React from "react";
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Layout from "./components/Layout/layout";
import Main from "./pages/main/main";
import ApisPage from "./pages/apis/apis";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Main />} />
          <Route path="/apis" element={<ApisPage />} />
          <Route path="/add-api" element={<ApisPage />} />
          <Route path="*" element={<Navigate to={"/"} />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;

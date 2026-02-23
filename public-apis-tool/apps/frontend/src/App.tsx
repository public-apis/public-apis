import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Layout from "./components/Layout/layout";
import Main from "./pages/main/main";
import ApisPage from "./pages/apis/apis";
import AddApi from "./pages/add-api/add-api";
import AuthSuccess from "./pages/auth/auth-success";
import { useStore } from "./store";
import { useEffect, useState } from "react";
import { apiClient } from "./api/api-client";
import { GET_ME } from "./utils/constants";
import { BeatLoader } from "react-spinners";

function App() {
  const [loading, setLoading] = useState(true);

  const setUser = useStore((state) => state.setUser);
  const clearUser = useStore((state) => state.clearUser);

  const getMe = async () => {
    await apiClient
      .get(GET_ME, { withCredentials: true })
      .then((res) => {
        console.log(res.data.user);
        setUser(res.data.user);
      })
      .catch((err) => {
        console.log(err);
        clearUser();
      })
      .finally(() => {
        setLoading(false);
      });
  };

  useEffect(() => {
    getMe();
  }, []);

  if (loading)
    return (
      <div className="flex items-center justify-center w-full h-screen overflow-hidden">
        <BeatLoader color="#1d4ed8" size={18} />
      </div>
    );

  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Main />} />
          <Route path="/apis" element={<ApisPage />} />
          <Route path="/add-api" element={<AddApi />} />
        </Route>

        <Route path="/auth-success" element={<AuthSuccess />} />

        <Route path="*" element={<Navigate to={"/"} />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

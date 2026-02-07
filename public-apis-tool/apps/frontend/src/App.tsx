import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Layout from "./components/Layout/layout";
import Main from "./pages/main/main";
import ApisPage from "./pages/apis/apis";
import AddApi from "./pages/add-api/add-api";
import AuthSuccess from "./pages/auth/auth-success";
import { useStore } from "./store";
import { useEffect } from "react";
import { toast } from "sonner";
import { apiClient } from "./api/api-client";
import { GET_ME } from "./utils/constants";

function App() {
  const { setUser, clearUser } = useStore();
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
      });
  };
  useEffect(() => {
    getMe();
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Main />} />
          <Route path="/apis" element={<ApisPage />} />
          <Route path="/add-api" element={<AddApi />} />
          <Route path="*" element={<Navigate to={"/"} />} />
        </Route>

        <Route path="/auth-success" element={<AuthSuccess />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

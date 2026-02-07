import { apiClient } from "@/api/api-client";
import { useStore } from "@/store";
import { GET_ME } from "@/utils/constants";
import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "sonner";

const AuthSuccess = () => {
  const { setUser, clearUser } = useStore();
  const navigate = useNavigate();
  const getMe = async () => {
    await apiClient
      .get(GET_ME, { withCredentials: true })
      .then((res) => {
        setUser(res.data.user);
        toast.success("Authorization successful");
      })
      .catch((err) => {
        console.log(err);
        clearUser();
        toast.error("Authorization failed");
      })
      .finally(() => {
        navigate("/add-api");
      });
  };
  useEffect(() => {
    getMe;
  }, []);
  return <div>AuthSuccess</div>;
};

export default AuthSuccess;

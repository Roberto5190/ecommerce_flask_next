import api from "./api";
import { saveToken, clearToken } from "@/utils/helpers";

export const login = async (email, password) => {
    const { data } = await api.post("/api/auth/login", { email, password });
    saveToken(data.token);
    return data;
};

export const register = (payload) => api.post("/api/auth/register", payload);

export const logout = () => clearToken();

import axios from "axios";
import { API_BASE } from "@/utils/constants";
import { getToken } from "@/utils/helpers";

const api = axios.create({
    baseURL: API_BASE,          // http://localhost:5000
    timeout: 8000,
});

// ▸ inyectar token si existe
api.interceptors.request.use((config) => {
    const token = getToken();
    if (token) config.headers.Authorization = `Bearer ${token}`;
    return config;
});

export default api;

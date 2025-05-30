export const saveToken = (t) => localStorage.setItem("token", t);
export const getToken  = () => (typeof window !== "undefined" ? localStorage.getItem("token") : null);
export const clearToken = () => localStorage.removeItem("token");

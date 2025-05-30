import api from "./api";

export const fetchProducts = (q = "") =>
    api.get("/api/products/", { params: { q } }).then((r) => r.data);

export const fetchProduct = (id) =>
    api.get(`/api/products/${id}`).then((r) => r.data);

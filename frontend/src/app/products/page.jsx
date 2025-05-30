"use client";

import { fetchProducts } from "@/services/products";
import ProductList from "@/components/products/ProductList";
import ProductFilter from "@/components/products/ProductFilter";
import { useState, useEffect } from "react";
import Loading from "@/components/common/Loading";

export default function ProductsPage() {
    const [allProducts, setAllProducts] = useState([])
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);

    // Carga inicial de productos
    useEffect(() => {
        (async () => {
            const data = await fetchProducts()
            setAllProducts(data)
            setProducts(data) //muestra todos los productos
            setLoading(false)
        })()
    }, [])

    // callback que viene del filtro
    const handleSearch = (q) => {
        const term = q.trim().toLowerCase();
        if (!term) return setProducts(allProducts);

        const filtered = allProducts.filter((p) =>
            p.name.toLowerCase().includes(term)
        );
        setProducts(filtered);
    };


    return (
        <section>
            <h2 className="text-2xl font-bold mb-4">Productos</h2>
            <ProductFilter onSearch={handleSearch} />
            {loading ? <Loading /> : <ProductList products={products} />}
        </section>
    );
}

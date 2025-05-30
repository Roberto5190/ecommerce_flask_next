"use client";

import ProductCard from "./ProductCard";

export default function ProductList({ products }) {
    if (!products.length) return <p>No se encontraron productos.</p>;

    return (
        <div className="grid grid-cols-[repeat(auto-fill,minmax(220px,1fr))] gap-6">
            {products.map((p) => (
                <ProductCard key={p.id} product={p} />
            ))}
        </div>
    );
}

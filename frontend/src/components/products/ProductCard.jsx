"use client";

import { useCart } from "@/context/CartContext";

export default function ProductCard({ product }) {
    const { addItem } = useCart();

    return (
        <div className="border rounded-xl p-4 flex flex-col gap-3 shadow-sm">
            <h3 className="text-lg font-semibold">{product.name}</h3>
            <p className="text-sm text-gray-500 flex-1 line-clamp-2">{product.description}</p>
            <span className="text-emerald-600 font-bold">${product.price.toFixed(2)}</span>
            
            <button
                onClick={() => addItem(product, 1)}
                className="bg-emerald-600 hover:bg-emerald-700 text-white rounded-md py-2"
            >
                Añadir al carrito
            </button>
        </div>
    );
}

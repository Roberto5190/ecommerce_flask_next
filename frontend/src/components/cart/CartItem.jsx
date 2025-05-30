"use client";

import { useCart } from "@/context/CartContext";

export default function CartItem({ item }) {
    const { minItem, addItem, removeItem } = useCart();
    const { product, quantity } = item;

    return (
        <li className="flex items-center justify-between gap-4 py-2 border-b">
            <div className="flex ">
                <p>IMG</p>
                <div className="flex-1">
                    <h4 className="font-semibold">{product.name}</h4>
                    <p className="text-sm text-gray-500">
                        ${product.price.toFixed(2)} × {quantity}
                    </p>
                </div>
            </div>


            <div className="flex items-center gap-2">
                <button
                    onClick={() => minItem(product, 1)}
                    className="px-2 rounded bg-emerald-600 text-white"
                >
                    -
                </button>
                <button
                    onClick={() => addItem(product, 1)}
                    className="px-2 rounded bg-emerald-600 text-white"
                >
                    +
                </button>
                <button
                    onClick={() => removeItem(product.id)}
                    className="px-2 rounded bg-red-600 text-white"
                >
                    🗑
                </button>
            </div>
        </li>
    );
}

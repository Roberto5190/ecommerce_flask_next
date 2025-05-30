"use client";

import { useCart } from "@/context/CartContext";

export default function CartSummary() {
    const { total, items } = useCart();

    if (!items.length) return null;

    return (
        <div className="mt-6 text-right space-y-3">
            <p className="text-lg">
                Total: <span className="font-bold">${total.toFixed(2)}</span>
            </p>
            <a
                href="/checkout"
                className="inline-block bg-emerald-600 hover:bg-emerald-700 text-white rounded-md px-5 py-2"
            >
                Ir a pagar
            </a>
        </div>
    );
}

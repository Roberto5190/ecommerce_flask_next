'use client'
import { useCart } from "@/context/CartContext";
import Link from "next/link";

export default function Header() {
    const { items } = useCart();
    const count = items.reduce((sum, it) => sum + it.quantity, 0);

    return (
        <header className="bg-emerald-600 text-white px-4 py-3 flex justify-between">
            <Link href="/" className="text-xl font-semibold">
                Mi Tienda
            </Link>

            <Link href="/cart" className="relative">
                🛒
                {count > 0 && (
                    <span className="absolute -top-2 -right-2 bg-red-600 rounded-full text-xs px-1">
                        {count}
                    </span>
                )}
            </Link>
        </header>
    );
}

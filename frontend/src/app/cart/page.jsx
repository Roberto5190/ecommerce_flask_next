"use client";

import { useCart } from "@/context/CartContext";
import CartItem from "@/components/cart/CartItem";
import CartSummary from "@/components/cart/CartSummary";

export default function CartPage() {
    const { items } = useCart();

    return (
        <section>
            <h2 className="text-2xl font-bold mb-4">Tu carrito</h2>

            {!items.length ? (
                <p>El carrito está vacío.</p>
            ) : (
                <>
                    <ul>
                        {items.map((it) => (
                            <CartItem key={it.product.id} item={it} />
                        ))}
                    </ul>

                    <CartSummary />
                </>
            )}
        </section>
    );
}

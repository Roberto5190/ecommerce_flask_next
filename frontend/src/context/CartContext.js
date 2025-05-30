"use client";
import { createContext, useContext, useEffect, useState } from "react";

const CartContext = createContext(null);

export function CartProvider({ children }) {
    const [items, setItems] = useState([]);

    // cargar de localStorage
    useEffect(() => {
        const saved = JSON.parse(localStorage.getItem("cart") || "[]");
        setItems(saved);
    }, []);

    // persistir cada cambio
    useEffect(() => {
        localStorage.setItem("cart", JSON.stringify(items));
    }, [items]);

    const addItem = (product, quantity = 1) => {
        setItems((prev) => {
            const found = prev.find((it) => it.product.id === product.id);
            
            if (found) {
                return prev.map((it) => {
                    if (it.product.id == product.id && it.quantity <= (it.product.stock - 1) ) {
                        return {
                            ...it,
                            quantity: it.quantity + quantity 
                        }
                    }
                    return it
            });
            }
            return [...prev, { product, quantity }];
        });
    };

    const minItem = (product, quantity = 1) => {
        setItems((prev) => {
            const found = prev.find((it) => it.product.id === product.id);
            if (found) {
                return prev.map((it) => {
                    ;
                    
                    if (it.product.id == product.id && it.quantity > 1) {
                        return {
                            ...it,
                            quantity: it.quantity - quantity 
                        }
                    }
                    return it
                });
            }
            return [...prev, { product, quantity }];
        });
    };

    const removeItem = (id) => setItems((prev) => prev.filter((it) => it.product.id !== id));

    const clear = () => setItems([]);

    const total = items.reduce((sum, it) => sum + it.product.price * it.quantity, 0);

    return (
        <CartContext.Provider value={{ items, minItem,  addItem, removeItem, clear, total }}>
            {children}
        </CartContext.Provider>
    );
}

export const useCart = () => useContext(CartContext);

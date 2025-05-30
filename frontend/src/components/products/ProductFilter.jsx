"use client";

import { useState } from "react";

export default function ProductFilter({ onSearch }) {
    const [q, setQ] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        onSearch(q);
    };

    return (
        <form onSubmit={handleSubmit} className="mb-6 flex gap-3">
            <input
                type="text"
                placeholder="Buscar..."
                value={q}
                onChange={(e) => setQ(e.target.value)}
                className="border rounded-md px-3 py-2 flex-1"
            />
            <button className="bg-slate-800 text-white rounded-md px-4">
                Filtrar
            </button>
        </form>
    );
}

"use client";
import { createContext, useState, useEffect, useContext } from "react";
import { login as apiLogin, logout as apiLogout } from "@/services/auth";
import { getToken } from "@/utils/helpers";
import {jwtDecode} from "jwt-decode";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);

    // autorrecuperar sesión
    useEffect(() => {
        const token = getToken();
        if (token) {
            try {
                const decoded = jwtDecode(token);
                setUser({ id: decoded.sub, username: decoded.username, token });
            } catch {
                apiLogout();
            }
        }
    }, []);

    const login = async (email, password) => {
        const { token } = await apiLogin(email, password);
        const decoded = jwtDecode(token);
        setUser({ id: decoded.sub, username: decoded.username, token });
    };

    const logout = () => {
        apiLogout();
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}

export const useAuth = () => useContext(AuthContext);

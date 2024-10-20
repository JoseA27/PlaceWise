// Este codigo no es funcional, solo es un ejemplo de como AuthContext podria ser implementado en el proyecto

import React, { createContext, useState, useContext } from 'react';

// Create a context for authentication
const AuthContext = createContext();

// AuthProvider component to wrap around the parts of the app that need access to auth state
export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    const login = (userData) => {
        setUser(userData);
    };

    const logout = () => {
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

// Custom hook to use the AuthContext
export const useAuth = () => {
    return useContext(AuthContext);
};
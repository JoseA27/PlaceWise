//Este codigo no es funcional, es un ejemplo de como GlobalContext podria ser implementado en el proyecto 

import React, { createContext, useReducer } from 'react';

// Initial state
const initialState = {
    user: null,
    isAuthenticated: false,
};

// Create context
export const GlobalContext = createContext(initialState);

// Reducer
const globalReducer = (state, action) => {
    switch (action.type) {
        case 'SET_USER':
            return {
                ...state,
                user: action.payload,
                isAuthenticated: true,
            };
        case 'LOGOUT':
            return {
                ...state,
                user: null,
                isAuthenticated: false,
            };
        default:
            return state;
    }
};

// Provider component
export const GlobalProvider = ({ children }) => {
    const [state, dispatch] = useReducer(globalReducer, initialState);

    // Actions
    const setUser = (user) => {
        dispatch({ type: 'SET_USER', payload: user });
    };

    const logout = () => {
        dispatch({ type: 'LOGOUT' });
    };

    return (
        <GlobalContext.Provider
            value={{
                user: state.user,
                isAuthenticated: state.isAuthenticated,
                setUser,
                logout,
            }}
        >
            {children}
        </GlobalContext.Provider>
    );
};
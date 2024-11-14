import React, { createContext, useState, useContext, useEffect } from "react";

// Crear el contexto de autenticación
const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext); // Hook para acceder al contexto

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Verificar si hay un token en localStorage al cargar la app
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      setIsAuthenticated(true); // Si hay token, el usuario está autenticado
    }
  }, []);

  const login = (token) => {
    setIsAuthenticated(true);
    localStorage.setItem("token", token);
  };

  const logout = () => {
    setIsAuthenticated(false);
    localStorage.removeItem("token"); 
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children} {/* Envolvemos el contenido de la aplicación */}
    </AuthContext.Provider>
  );
};

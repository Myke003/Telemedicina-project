import React, { useState } from "react";
import "./Header.css"; // Asegúrate de tener un archivo CSS para los estilos
import { useAuth } from "../../js/context/AuthContext"; // Asegúrate de que la ruta sea correcta
import { useNavigate } from "react-router-dom"; // Para redirigir al login

let userName = "User";

const Header = () => {
  const { logout } = useAuth(); // Obtén la función logout del contexto
  const [isUserMenuOpen, setUserMenuOpen] = useState(false);
  const [isNotificationsOpen, setNotificationsOpen] = useState(false);
  const navigate = useNavigate(); // Para redirigir a la página de login

  const handleLogout = () => {
    logout(); // Marca al usuario como no autenticado
    console.log("Cerrando sesión...");
    navigate("/login"); // Redirige al usuario a la página de login
  };

  const toggleUserMenu = () => {
    setUserMenuOpen(!isUserMenuOpen);
  };

  const toggleNotifications = () => {
    setNotificationsOpen(!isNotificationsOpen);
  };

  return (
    <header className="header">
      <div className="header-right">
        {/* Notifications Section */}
        <div className="notifications" onClick={toggleNotifications}>
          <i className="bi bi-bell-fill"></i>
          <span className="notification-count">0</span>
        </div>

        {/* Notifications Dropdown */}
        {isNotificationsOpen && (
          <div className="notifications-menu">
            <ul>
              <li>No tienes nuevas notificaciones</li>
            </ul>
          </div>
        )}

        {/* User Profile Section */}
        <div className="user-profile" onClick={toggleUserMenu}>
          <i className="bi bi-person-circle"></i>
          <span className="user-name">{userName}</span>
        </div>

        {/* Dropdown Menu for User */}
        {isUserMenuOpen && (
          <div className="user-menu">
            <ul>
              <li>Mi perfil</li>
              <li onClick={handleLogout}>Cerrar sesión</li> {/* Llama a handleLogout al hacer clic */}
            </ul>
          </div>
        )}
      </div>
    </header>
  );
};

export default Header;

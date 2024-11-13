import React, { useState } from "react";
import { Link, useLocation } from "react-router-dom";
import "./sidebar.css";

const Sidebar = () => {
  const [isExpanded, setIsExpanded] = useState(true);
  const location = useLocation(); // Para obtener la ruta actual

  const menuItems = [
    { path: "/", label: "Inicio", icon: "bi bi-house-door" },
    { path: "/appointments", label: "Agendar Cita", icon: "bi bi-folder-plus" },
    { path: "/agenda", label: "Agenda", icon: "bi bi-calendar-event" },
    { path: "/video-call", label: "Videollamada", icon: "bi bi-camera-video" },
    { path: "/chat", label: "Chat", icon: "bi bi-chat" },
    { path: "/medical-history", label: "Historial Médico", icon: "bi bi-file-earmark-medical" },
    { path: "/prescription", label: "Recetas", icon: "bi bi-receipt" },
  ];

  const toggleSidebar = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <aside className={`sidebar ${isExpanded ? "expanded" : "collapsed"}`}>
      <div className="sidebar-header">
        <div className="logo-container">
          {isExpanded ? (
            <h1 className="logo">TeleMed</h1>
          ) : (
            <i className="bi bi-arrow-bar-right toggle-icon" onClick={toggleSidebar}></i> // Icono de expansión cuando el sidebar está colapsado
          )}
        </div>
        {isExpanded && (
          <button className="toggle-btn" onClick={toggleSidebar}>
            {"<<"}
          </button>
        )}
      </div>
      <nav>
        <ul className="sidebar-links-container">
          {menuItems.map((item, index) => (
            <li
              key={index}
              className={`sidebar-link ${location.pathname === item.path ? "active" : ""}`} // Agrega la clase "active"
            >
              <Link to={item.path}>
                <i className={`${item.icon} icon-style`}></i>
                {isExpanded && <span className="label">{item.label}</span>}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;

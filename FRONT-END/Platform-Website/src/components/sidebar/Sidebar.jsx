import React from "react";
import { Link } from "react-router-dom";
import './sidebar.css';

const Sidebar = () => {
  const menuItems = [
    { path: "/", label: "Inicio" },
    { path: "/profile", label: "Agenda" },
    { path: "/video-call", label: "Videollamada" },
    { path: "/chat", label: "Chat" },
    { path: "/medical-history", label: "Historial Médico" },
    { path: "/prescription", label: "Recetas" },
  ];

  return (
    <aside className="sidebar">
      <nav>
        <div className="logo-container">
          <h1>TeleMed</h1>
        </div>
        <ul className="sidebar-links-container">
          {menuItems.map((item, index) => (
            <li key={index}>
              <Link to={item.path}>{item.label}</Link>
            </li>
          ))}
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;

// src/Components/Sidebar/Sidebar.jsx
import React from "react";
import './SideBar.css'; // Importamos el archivo CSS

const Sidebar = () => {
  return (
    <nav className="sidebar bg-body-tertiary">
      <h2 className="sidebar-title">TeleMed</h2>
      <ul className="sidebar-list">
        <li><a className="sidebar-item" href="#">Inicio</a></li>
        <li><a className="sidebar-item" href="#">Citas</a></li>
        <li><a className="sidebar-item" href="#">Perfil</a></li>
        <li><a className="sidebar-item" href="#">Historial Médico</a></li>

      </ul>
    </nav>
  );
};

export default Sidebar;

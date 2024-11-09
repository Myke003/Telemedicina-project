import React from "react";
import "./profilemenu.css";

const ProfileMenu = ({ toggleDarkMode, isDarkMode }) => {
  return (
    <div className="profile-menu">
      <button onClick={toggleDarkMode}>
        {isDarkMode ? "Modo Claro" : "Modo Oscuro"}
      </button>
      <button onClick={() => alert("Cerrar sesión")}>Cerrar sesión</button>
    </div>
  );
};

export default ProfileMenu;

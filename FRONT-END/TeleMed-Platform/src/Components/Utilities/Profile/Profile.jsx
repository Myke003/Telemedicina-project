import React from "react";
import "./Profile.css"; // Importamos el archivo CSS

const Profile = () => {
  return (
    <div className="profile-container d-flex align-items-center">
      <div className="dropdown d-flex align-item-center justify-content-center">
        <button
          className="btn dropdown-toggle"
          type="button"
          id="dropdownMenuButton"
          data-bs-toggle="dropdown"
          aria-expanded="false"
        >
          <img
            src="https://picsum.photos/200" // Cambia esto por la URL de la imagen de perfil
            alt="Perfil"
            className="rounded-circle profile-image"
          />
          Usuario
        </button>
        <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton">
          <li>
            <a className="dropdown-item" href="#/perfil">
              Ver Perfil
            </a>
          </li>
          <li>
            <a className="dropdown-item" href="#/ajustes">
              Ajustes
            </a>
          </li>
          <li>
            <a className="dropdown-item" href="#/logout">
              Cerrar sesión
            </a>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Profile;

// src/Components/Dashboard/Dashboard.jsx
import React from "react";
import NavBar from "../NavBar/NavBar";
import SideBar from "../SideBar/SideBar";
import './Dashboard.css'; // Importa el archivo CSS

const Dashboard = () => {
  return (
    <div className="dashboard-container">
      <NavBar />
      <SideBar />
      <main className="main-content">
        {/*Contenido principal*/}
        <h1>Contenido Principal</h1>
      </main>
    </div>
  );
};

export default Dashboard;

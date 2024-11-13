// src/pages/Layout/Layout.jsx
import React from "react";
import { Outlet } from "react-router-dom";
import Header from "../../components/header/Header"; // Subir dos niveles para llegar a src/components
import Sidebar from "../../components/sidebar/sidebar"; // Similar

const Layout = () => {
  return (
    <div className="app-container">
      <Sidebar />
      <div className="main-content">
        <Header />
        <div className="page-content">
          <Outlet />{" "}
          {/* Aquí se renderizan las páginas como Home, Profile, etc. */}
        </div>
      </div>
    </div>
  );
};

console.log("hgola")

export default Layout;

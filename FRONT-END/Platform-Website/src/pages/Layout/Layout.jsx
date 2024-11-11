// src/pages/Layout/Layout.jsx
import React from "react";
import { Outlet } from "react-router-dom";
import Header from "../../components/header/header"; // Subir dos niveles para llegar a src/components
import Sidebar from "../../components/sidebar/sidebar"; // Similar
import Footer from "../../components/footer/footer"; // Similar

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
        <Footer />
      </div>
    </div>
  );
};

console.log("hgola")

export default Layout;

// src/App.jsx
import React from "react";
import AppRoutes from "./routes/AppRoutes";
import Header from "./components/header/Header";
import Sidebar from "./components/sidebar/Sidebar";
import Footer from "./components/footer/Footer";
import "./App.css";

const App = () => {
  return (
    <div className="app-container">
      <Sidebar />
      <div className="main-content">
        <Header />
        <div className="page-content">
          <AppRoutes />
        </div>
        <Footer />
      </div>
    </div>
  );
};

export default App;

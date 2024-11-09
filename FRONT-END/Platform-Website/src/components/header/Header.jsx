// src/components/Header.jsx
import React from "react";
import UserProfile from "../profile/UserProfile";

const phrases = "Tu solución al instante";

const Header = () => {
  return (
    <>
      <header className="header">
        <div className="text-container">{phrases}</div>
      </header>
      <UserProfile />
    </>
  );
};

export default Header;

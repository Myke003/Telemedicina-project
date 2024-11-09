import React, { useState } from "react";
import ProfileMenu from "./ProfileMenu";
import "./userprofile.css";

const UserProfile = ({ toggleDarkMode, isDarkMode }) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <>
      <img
        className="profile-img"
        src="https://via.placeholder.com/40"
        alt="Usuario"
      />
      <span className="username">Miguel</span>
    </>
  );
};

export default UserProfile;

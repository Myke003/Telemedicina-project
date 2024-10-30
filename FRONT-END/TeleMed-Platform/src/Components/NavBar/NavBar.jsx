import React from "react";
import Profile from "../Utilities/Profile/Profile";
import Notification from "../Utilities/Notifications/Notification";

const NavBar = () => {
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-fluid d-flex justify-content-end">
        <div className="navbar-nav">
          <Notification />
          <Profile />
        </div>
      </div>
    </nav>
  );
};

export default NavBar;

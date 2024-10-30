import React from "react";
import './Notification.css'; 

const Notification = ({ message }) => {
  return (
    <div className="notification d-flex align-items-center justify-content-center">
      <i className="bi bi-bell-fill notification-icon"></i>
    </div>
  );
};
export default Notification;

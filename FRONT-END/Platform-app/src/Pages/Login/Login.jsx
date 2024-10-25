import React from 'react';
import './login.css';
import LoginForm from './Login-components/LoginForm';

function Login() {
  return (
    <div className="container-layout">
      <div className="login-container">
        <LoginForm/>
      </div>
      <div className="login-layout">
      </div>
    </div>
  );
}

export default Login;

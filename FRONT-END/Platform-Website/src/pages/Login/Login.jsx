import React, { useState } from "react";
import { Button, TextField, Paper, Typography, Box } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../js/context/AuthContext";
import "./login.css";

const Login = () => {
  const navigate = useNavigate();
  const { login } = useAuth(); // Obtén la función login del contexto
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  // Funciones para actualizar los estados de email y contraseña
  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!email || !password) {
      alert("Por favor, ingresa tu correo y contraseña.");
      return;
    }

    // Lógica de autenticación (puedes reemplazar esto con un backend real)
    if (email === "admin" && password === "admin") {
      alert("Iniciaste sesión");
      login(); // Marca al usuario como autenticado
      navigate("/"); // Redirige a la página principal después del login
    } else {
      alert("Usuario y/o contraseña incorrecto");
    }
  };

  return (
    <div className="login-wrapper">
      <Paper elevation={3} className="login-container">
        <div className="logo-container">
          <img src="logo.png" alt="TeleMed Logo" className="logo" />
        </div>
        <Typography variant="h4" component="h1" color="primary" gutterBottom>
          Bienvenido a TeleMed
        </Typography>
        <Typography
          variant="subtitle1"
          component="p"
          color="textSecondary"
          gutterBottom
        >
          Ingresa tus credenciales para acceder a nuestra plataforma de salud
        </Typography>
        <form onSubmit={handleSubmit} className="input-container">
          <TextField
            className="input-login"
            id="outlined"
            label="Email"
            variant="outlined"
            onChange={handleEmailChange}
            value={email}
            required
          />
          <TextField
            className="input-login"
            id="outlined-password-input"
            label="Contraseña"
            type="password"
            variant="outlined"
            onChange={handlePasswordChange}
            value={password}
            required
          />
          <Button
            type="submit"
            className="login-btn"
            variant="contained"
            color="primary"
          >
            Iniciar sesión
          </Button>
        </form>
        <Box className="footer-container">
          <Typography
            variant="body2"
            className="login-text"
            onClick={() => navigate("/forgotPassword")}
          >
            ¿Olvidaste tu contraseña?
          </Typography>
          <Typography
            variant="body2"
            className="login-text"
            onClick={() => navigate("/register")}
          >
            Regístrate aquí
          </Typography>
        </Box>
      </Paper>
    </div>
  );
};

export default Login;

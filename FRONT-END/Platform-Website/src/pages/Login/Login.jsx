import React, { useState } from "react";
import { Button, TextField, Paper, Typography, Box } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../js/context/AuthContext";
import axios from "axios";  // Asegúrate de importar axios
import "./login.css";

const Login = () => {
  const navigate = useNavigate();
  const { login } = useAuth(); // Obtén la función login del contexto
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");  // Para manejar errores

  // Funciones para actualizar los estados de email y contraseña
  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!email || !password) {
      alert("Por favor, ingresa tu correo y contraseña.");
      return;
    }

    try {
      // Realiza la petición al backend para autenticar al usuario
      const response = await axios.post("http://127.0.0.1:5000/login", {
        email,
        password
      });

      // El backend debería devolver el token en la respuesta
      const token = response.data.token;

      // Guardar el token en el localStorage o contexto
      localStorage.setItem("token", token);  // Almacenar el token

      login();  // Marca al usuario como autenticado en el contexto
      navigate("/"); // Redirige a la página principal después del login
    } catch (err) {
      // Manejo de errores
      setError("Usuario y/o contraseña incorrecto");
      console.error("Error de login:", err);
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
        {error && <Typography color="error">{error}</Typography>}
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

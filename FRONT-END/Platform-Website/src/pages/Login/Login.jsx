import React, { useState } from 'react';
import { Button, TextField, Paper, Typography, Box } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import './login.css';

const Login = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!email || !password) {
      alert('Por favor, ingresa tu correo y contraseña.');
      return;
    }

    // Aquí podrías agregar la lógica de autenticación (API, etc.)
    console.log('Email:', email);
    console.log('Password:', password);

    if (email === 'admin' && password === 'admin') {
      console.log('Iniciaste sesion');
      alert('Iniciaste sesion');
      navigate('/');
    } else {
      console.log('Usuario y/o contraseña incorrecto');
      alert('Usuario y/o contraseña incorrecto');
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
        <Typography variant="subtitle1" component="p" color="textSecondary" gutterBottom>
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
          <Button type="submit" className="login-btn" variant="contained" color="primary">
            Iniciar sesión
          </Button>
        </form>
        <Box className="footer-container">
          <Typography variant="body2" className="login-text" onClick={() => navigate('/forgotPassword')}>
            ¿Olvidaste tu contraseña?
          </Typography>
          <Typography variant="body2" className="login-text" onClick={() => navigate('/register')}>
            Regístrate aquí
          </Typography>
        </Box>
      </Paper>
    </div>
  );
};

export default Login;
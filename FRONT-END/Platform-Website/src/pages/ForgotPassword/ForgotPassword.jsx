import React, { useState } from 'react';
import { Button, TextField, Paper, Typography, Box } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import './forgotPassword.css';

const ForgotPassword = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!email) {
      alert('Por favor, ingresa tu correo.');
      return;
    }

    // Aquí podrías agregar la lógica de recuperación de contraseña (API, etc.)
    console.log('Email:', email);
    alert('Se ha enviado un correo para restablecer tu contraseña.');
    navigate('/login');
  };

  return (
    <div className="forgotPassword-wrapper">
      <Paper elevation={3} className="forgotPassword-container">
        <div className="logo-container">
          <img src="logo.png" alt="TeleMed Logo" className="logo" />
        </div>
        <Typography variant="h4" component="h1" color="primary" gutterBottom>
          Recuperar contraseña
        </Typography>
        <Typography variant="subtitle1" component="p" color="textSecondary" gutterBottom>
          Ingresa tu correo electrónico
        </Typography>
        <form onSubmit={handleSubmit} className="input-container">
          <TextField
            className="input-forgotPassword"
            id="outlined"
            label="Email"
            variant="outlined"
            onChange={handleEmailChange}
            value={email}
            required
          />
          <Button type="submit" className="forgotPassword-btn" variant="contained" color="primary">
            Enviar
          </Button>
        </form>
        <Box className="footer-container">
          <Typography variant="body2" className="forgotPassword-text" onClick={() => navigate('/login')}>
            Volver al inicio de sesión
          </Typography>
        </Box>
      </Paper>
    </div>
  );
};

export default ForgotPassword;
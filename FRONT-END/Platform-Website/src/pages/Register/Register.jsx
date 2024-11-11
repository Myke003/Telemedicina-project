import React, { useState } from 'react';
import { Button, TextField, Paper, Typography, Box } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import './register.css';

const Register = () => {
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleNameChange = (e) => {
    setName(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleConfirmPasswordChange = (e) => {
    setConfirmPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!name || !email || !password || !confirmPassword) {
      alert('Por favor, llena todos los campos.');
      return;
    }

    if (password !== confirmPassword) {
      alert('Las contraseñas no coinciden.');
      return;
    }

    // Aquí podrías agregar la lógica de registro (API, etc.)
    console.log('Name:', name);
    console.log('Email:', email);
    console.log('Password:', password);
    console.log('Confirm Password:', confirmPassword);
    alert('Registro exitoso. Inicia sesión.');
    navigate('/login');
  };

  return (
    <div className="register-wrapper">
      <Paper elevation={3} className="register-container">
        <div className="logo-container">
          <img src="logo.png" alt="TeleMed Logo" className="logo" />
        </div>
        <Typography variant="h4" component="h1" color="primary" gutterBottom>
          Registro
        </Typography>
        <Typography variant="subtitle1" component="p" color="textSecondary" gutterBottom>
          Crea tu cuenta en TeleMed
        </Typography>
        <form onSubmit={handleSubmit} className="input-container">
          <TextField
            className="input-register"
            id="outlined"
            label="Nombre"
            variant="outlined"
            onChange={handleNameChange}
            value={name}
            required
          />
          <TextField
            className="input-register"
            id="outlined"
            label="Email"
            variant="outlined"
            onChange={handleEmailChange}
            value={email}
            required
          />
          <TextField
            className="input-register"
            id="outlined-password-input"
            label="Contraseña"
            type="password"
            variant="outlined"
            onChange={handlePasswordChange}
            value={password}
            required
          />
          <TextField
            className="input-register"
            id="outlined-password-input"
            label="Confirmar contraseña"
            type="password"
            variant="outlined"
            onChange={handleConfirmPasswordChange}
            value={confirmPassword}
            required
          />
          <Button type="submit" className="register-btn" variant="contained" color="primary">
            Registrarse
          </Button>
        </form>
        <Box className="footer-container">
          <Typography variant="body2" className="register-text" onClick={() => navigate('/login')}>
            ¿Ya tienes una cuenta? Inicia sesión
          </Typography>
        </Box>
      </Paper>
    </div>
  );
};

export default Register;
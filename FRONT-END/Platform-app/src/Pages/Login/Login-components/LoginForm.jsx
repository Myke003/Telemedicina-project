import React from 'react';
import InputGroup from './InputGroup';

function LoginForm() {
   return (
    <form method='post' className='login'>
      <div className="brand-logo">
         <h1>TeleMed</h1>
      </div>
      <div className="title-box">
         <p>¡Bienvenido!</p>
      </div>
      <InputGroup type="text" placeholder="Ingresa tu usuario" icon="bi-person-circle" />
      <InputGroup type="password" placeholder="Ingresa tu contraseña" icon="bi-lock-fill" />
      <button type="button" className="btn btn-primary">Iniciar sesión</button>
    </form>
  );
};

export default LoginForm;
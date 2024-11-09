// src/components/Footer.jsx
import React from 'react';

const Footer = () => {
  return (
    <footer className="footer">
      <p>&copy; {new Date().getFullYear()} Plataforma de Telemedicina. Todos los derechos reservados.</p>
      {/* Puedes agregar enlaces de redes sociales, políticas de privacidad, etc. */}
    </footer>
  );
};

export default Footer;

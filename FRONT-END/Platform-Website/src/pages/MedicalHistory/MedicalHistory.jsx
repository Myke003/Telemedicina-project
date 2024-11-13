import React from 'react';
import './medicalHistory.css';

const MedicalHistory = () => {
  const history = [
    { date: '2024-10-10', doctor: 'Dr. Smith', diagnosis: 'Consulta general' },
    { date: '2024-11-05', doctor: 'Dr. Johnson', diagnosis: 'Chequeo' },
  ];

  return (
    <div className="medical-history-container">
      <h2>Historial Médico</h2>
      <div className="history-list">
        {history.map((record, index) => (
          <div key={index} className="history-card">
            <p><strong>Fecha:</strong> {record.date}</p>
            <p><strong>Médico:</strong> {record.doctor}</p>
            <p><strong>Diagnóstico:</strong> {record.diagnosis}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MedicalHistory;

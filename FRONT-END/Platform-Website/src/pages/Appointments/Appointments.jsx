import React, { useState, useEffect } from 'react';
import './Appointments.css';

const Appointments = () => {
  const [doctor, setDoctor] = useState('');
  const [availableDates, setAvailableDates] = useState([]);
  const [selectedDate, setSelectedDate] = useState('');
  const [availableTimes, setAvailableTimes] = useState([]);
  const [selectedTime, setSelectedTime] = useState('');

  useEffect(() => {
    // Simulamos la obtención de fechas disponibles para la cita (esto vendría de una API o base de datos)
    const fetchAvailableDates = () => {
      return [
        '2024-11-15',
        '2024-11-16',
        '2024-11-17'
      ];
    };

    setAvailableDates(fetchAvailableDates());
  }, []);

  useEffect(() => {
    if (selectedDate) {
      // Simulamos la obtención de horas disponibles para la fecha seleccionada
      const fetchAvailableTimes = (date) => {
        return date === '2024-11-15'
          ? ['10:00 AM', '12:00 PM', '2:00 PM']
          : date === '2024-11-16'
          ? ['9:00 AM', '1:00 PM', '4:00 PM']
          : ['11:00 AM', '3:00 PM'];
      };

      setAvailableTimes(fetchAvailableTimes(selectedDate));
    }
  }, [selectedDate]);

  const handleSubmit = () => {
    // Aquí se procesaría la cita con la fecha y hora seleccionada
    console.log(`Cita agendada con el Dr. ${doctor} para el ${selectedDate} a las ${selectedTime}`);
  };

  return (
    <div className="appointments-container">
      <h2>Agendar Cita</h2>
      <div className="form-group">
        <label htmlFor="doctor">Selecciona un médico:</label>
        <input
          type="text"
          id="doctor"
          value={doctor}
          onChange={(e) => setDoctor(e.target.value)}
          placeholder="Nombre del médico"
        />
      </div>

      <div className="form-group">
        <label htmlFor="date">Selecciona una fecha:</label>
        <select
          id="date"
          value={selectedDate}
          onChange={(e) => setSelectedDate(e.target.value)}
        >
          <option value="">--Selecciona una fecha--</option>
          {availableDates.map((date, index) => (
            <option key={index} value={date}>
              {date}
            </option>
          ))}
        </select>
      </div>

      {selectedDate && (
        <div className="form-group">
          <label htmlFor="time">Selecciona una hora:</label>
          <select
            id="time"
            value={selectedTime}
            onChange={(e) => setSelectedTime(e.target.value)}
          >
            <option value="">--Selecciona una hora--</option>
            {availableTimes.map((time, index) => (
              <option key={index} value={time}>
                {time}
              </option>
            ))}
          </select>
        </div>
      )}

      <button
        type="button"
        onClick={handleSubmit}
        className="btn"
        disabled={!selectedTime || !selectedDate || !doctor}
      >
        Confirmar Cita
      </button>
    </div>
  );
};

export default Appointments;

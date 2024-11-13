// src/components/CalendarComponent.jsx
import React, { useState } from "react";
import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import "react-big-calendar/lib/css/react-big-calendar.css";
import "./calendarComponent.css"; // Archivo de estilos para personalizar el calendario

const localizer = momentLocalizer(moment);

const CalendarComponent = () => {
  const [events, setEvents] = useState([
    {
      title: "Cita con el Dr. Pérez",
      start: new Date(2024, 10, 15, 10, 0),
      end: new Date(2024, 10, 15, 11, 0),
    },
    {
      title: "Revisión general",
      start: new Date(2024, 10, 18, 14, 0),
      end: new Date(2024, 10, 18, 15, 0),
    },
  ]);

  return (
    <Calendar
      localizer={localizer}
      events={events}
      startAccessor="start"
      endAccessor="end"
      style={{ height: 500, margin: "20px 0" }}
    />
  );
};

export default CalendarComponent;

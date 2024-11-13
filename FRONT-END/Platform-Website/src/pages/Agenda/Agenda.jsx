import React from "react";
import CalendarComponent from "../../components/calendarComponent/CalendarComponent";

const Agenda = () => {
  return (
    <div className="video-call">
      <h2>Agenda</h2>
      <p>Mira las citas que vas a tener pronto.</p>
      <CalendarComponent />
    </div>
  );
};

export default Agenda;

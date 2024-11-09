// src/routes/AppRoutes.jsx
import { Routes, Route } from 'react-router-dom';
import Home from '../pages/Home';
import Profile from '../pages/Profile';
import Appointments from '../pages/Appointments';
import VideoCall from '../pages/VideoCall';
import Chat from '../pages/Chat';
import MedicalHistory from '../pages/MedicalHistory';
import Prescription from '../pages/Prescription';

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/profile" element={<Profile />} />
      <Route path="/appointments" element={<Appointments />} />
      <Route path="/video-call" element={<VideoCall />} />
      <Route path="/chat" element={<Chat />} />
      <Route path="/medical-history" element={<MedicalHistory />} />
      <Route path="/prescription" element={<Prescription />} />
    </Routes>
  );
};

export default AppRoutes;

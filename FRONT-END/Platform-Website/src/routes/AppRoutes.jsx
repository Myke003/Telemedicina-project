import { Routes, Route } from "react-router-dom";
import Home from "../pages/Home/Home";
import Profile from "../pages/Profile/Profile";
import Appointments from "../pages/Appointments/Appointments";
import VideoCall from "../pages/Videocall/VideoCall";
import Chat from "../pages/Chat/Chat";
import MedicalHistory from "../pages/MedicalHistory/MedicalHistory";
import Prescription from "../pages/Prescription/Prescription";
import Layout from "../pages/Layout/Layout";
import Login from "../pages/Login/Login";
import Register from "../pages/Register/Register";
import ForgotPassword from "../pages/ForgotPassword/ForgotPassword";

const AppRoutes = () => {
  return (
    <Routes>
      {/* Rutas públicas  (Login, register, etc) */}
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/forgotPassword" element={<ForgotPassword />} />

      {/* Rutas protegidas, disponibles despues de iniciar sesion*/}
      <Route element={<Layout />}>
        <Route path="/" element={<Home />} />
        <Route path="/home" element={<Home />} />{" "}
        <Route path="/profile" element={<Profile />} />{" "}
        <Route path="/appointments" element={<Appointments />} />{" "}
        <Route path="/video-call" element={<VideoCall />} />{" "}
        <Route path="/chat" element={<Chat />} />{" "}
        <Route path="/medical-history" element={<MedicalHistory />} />{" "}
        <Route path="/prescription" element={<Prescription />} />{" "}
      </Route>
    </Routes>
  );
};

export default AppRoutes;

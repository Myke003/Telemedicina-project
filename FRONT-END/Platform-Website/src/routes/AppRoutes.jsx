import { Routes, Route } from "react-router-dom";
import Home from "../pages/Home/Home";
import Appointments from "../pages/Appointments/Appointments";
import VideoCall from "../pages/Videocall/VideoCall";
import Chat from "../pages/Chat/Chat";
import MedicalHistory from "../pages/MedicalHistory/MedicalHistory";
import Prescription from "../pages/Prescription/Prescription";
import Layout from "../pages/Layout/Layout";
import Login from "../pages/Login/Login";
import Register from "../pages/Register/Register";
import ForgotPassword from "../pages/ForgotPassword/ForgotPassword";
import Agenda from "../pages/Agenda/Agenda";
import PrivateRoute from "./PrivateRoute"; // Asegúrate de importar PrivateRoute

const AppRoutes = () => {
  return (
    <Routes>
      {/* Rutas públicas */}
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/forgotPassword" element={<ForgotPassword />} />

      {/* Rutas protegidas */}
      <Route element={<Layout />}>
        <Route
          path="/"
          element={
            <PrivateRoute>
              <Home />
            </PrivateRoute>
          }
        />
        <Route
          path="/appointments"
          element={
            <PrivateRoute>
              <Appointments />
            </PrivateRoute>
          }
        />
        <Route
          path="/video-call"
          element={
            <PrivateRoute>
              <VideoCall />
            </PrivateRoute>
          }
        />
        <Route
          path="/chat"
          element={
            <PrivateRoute>
              <Chat />
            </PrivateRoute>
          }
        />
        <Route
          path="/medical-history"
          element={
            <PrivateRoute>
              <MedicalHistory />
            </PrivateRoute>
          }
        />
        <Route
          path="/prescription"
          element={
            <PrivateRoute>
              <Prescription />
            </PrivateRoute>
          }
        />
        <Route
          path="/agenda"
          element={
            <PrivateRoute>
              <Agenda />
            </PrivateRoute>
          }
        />
      </Route>
    </Routes>
  );
};

export default AppRoutes;

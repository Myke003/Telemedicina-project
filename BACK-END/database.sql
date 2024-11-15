CREATE DATABASE IF NOT EXISTS telemed_db;
USE telemed_db;

-- Crear tabla roles
CREATE TABLE IF NOT EXISTS roles (
  id INT(11) AUTO_INCREMENT PRIMARY KEY,
  role_name VARCHAR(50) NOT NULL UNIQUE,
  description TEXT
);

-- Crear tabla users
CREATE TABLE IF NOT EXISTS users (
  id INT(11) AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  name VARCHAR(100),
  role ENUM('patient', 'doctor', 'admin') DEFAULT 'patient',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Crear tabla user_roles
CREATE TABLE IF NOT EXISTS user_roles (
  user_id INT(11) NOT NULL,
  role_id INT(11) NOT NULL,
  PRIMARY KEY (user_id, role_id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (role_id) REFERENCES roles(id)
);

-- Crear tabla appointments
CREATE TABLE IF NOT EXISTS appointments (
  id INT(11) AUTO_INCREMENT PRIMARY KEY,
  patient_id INT(11),
  doctor_id INT(11),
  appointment_date DATETIME,
  status ENUM('pending', 'confirmed', 'cancelled', 'completed') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (patient_id) REFERENCES users(id),
  FOREIGN KEY (doctor_id) REFERENCES users(id)
);

-- Crear tabla medical_history
CREATE TABLE IF NOT EXISTS medical_history (
  id INT(11) AUTO_INCREMENT PRIMARY KEY,
  appointment_id INT(11),
  notes TEXT,
  diagnosis TEXT,
  prescription TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (appointment_id) REFERENCES appointments(id)
);

-- Crear tabla notifications
CREATE TABLE IF NOT EXISTS notifications (
  id INT(11) AUTO_INCREMENT PRIMARY KEY,
  user_id INT(11),
  type VARCHAR(50),
  message TEXT,
  status ENUM('unread', 'read') DEFAULT 'unread',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Crear tabla permissions
CREATE TABLE IF NOT EXISTS permissions (
  id INT(11) AUTO_INCREMENT PRIMARY KEY,
  role_id INT(11),
  permission_name VARCHAR(50),
  description TEXT,
  FOREIGN KEY (role_id) REFERENCES roles(id)
);

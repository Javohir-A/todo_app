-- Active: 1736361328546@@127.0.0.1@3306@Airport
CREATE DATABASE todo_app;
USE todo_app;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('Pending', 'Completed') DEFAULT 'Pending'
);
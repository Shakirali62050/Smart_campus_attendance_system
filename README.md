 Campus Attendance System using ML-Driven Face Recognition

A cloud-native attendance management system that automates student and faculty attendance tracking using Machine Learning-based Face Recognition. The application provides secure user registration, face capture, attendance marking, and administrative management through an intuitive web interface.

---

## 📖 Project Overview

The Smart Campus Attendance System eliminates manual attendance processes by leveraging facial recognition technology. Users can register their facial data, train the recognition model, and automatically mark attendance through webcam-based face detection.

The project is containerized using Docker and deployed on Kubernetes with CI/CD automation through Jenkins, ensuring scalability, reliability, and efficient application delivery.

---

## 🚀 Features

### 👨‍💼 Admin Features

* Secure Admin Login
* Student & Faculty Registration
* Face Data Capture via Webcam
* CNN Model Training
* Attendance Monitoring Dashboard
* User Management

### 👨‍🎓 Student & Faculty Features

* Face-based Attendance Marking
* Automated Attendance Recording
* Secure Authentication

### ⚙️ DevOps Features

* Docker Containerization
* Kubernetes Deployment
* Horizontal Pod Autoscaler (HPA)
* Jenkins CI/CD Pipeline
* GitHub Integration
* Automated Application Deployment

---

## 🛠️ Technology Stack

### Backend

* Python
* Flask
* OpenCV
* Machine Learning (CNN)

### Frontend

* HTML
* CSS
* JavaScript

### DevOps & Cloud

* Docker
* Kubernetes
* Jenkins
* GitHub
* Linux

### Version Control

* Git
* GitHub

---

## 🏗️ System Architecture

```text
                    +------------------+
                    |      Users       |
                    | Admin / Student  |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    | Flask Web App    |
                    | Login Dashboard  |
                    +--------+---------+
                             |
          +------------------+------------------+
          |                                     |
          v                                     v
+--------------------+              +----------------------+
| Face Registration  |              | Attendance Module    |
| Webcam Capture     |              | Face Recognition     |
+---------+----------+              +----------+-----------+
          |                                    |
          v                                    v
+--------------------+              +----------------------+
| Face Dataset       |              | CNN Face Model       |
| Storage            |              | Prediction Engine    |
+---------+----------+              +----------+-----------+
          |                                    |
          +------------------+-----------------+
                             |
                             v
                    +------------------+
                    | Attendance Data  |
                    | Records Storage  |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    | Admin Dashboard  |
                    | Attendance View  |
                    +------------------+

------------------------------------------------------------

GitHub
   |
   v
Jenkins Pipeline
   |
   v
Docker Build
   |
   v
Docker Image
   |
   v
Kubernetes Cluster
   |
   v
Smart Campus Attendance System
```

---

## 📷 Application Screenshots

### 🔐 Login Portal

The login portal allows administrators, students, and faculty members to securely access the attendance management system.





---

### 📊 Admin Dashboard

The administrator dashboard provides centralized management for user registration, model training, attendance monitoring, and system administration.



---

### 👤 User Registration

Students and faculty members can be registered into the system, followed by face data capture for recognition model training.



---

### 📸 Face Capture Module

The webcam-based face capture module collects facial images and prepares datasets for CNN model training.




## 🔄 CI/CD Pipeline

The application deployment process is fully automated using Jenkins.

### Pipeline Workflow

```text
Developer
    |
    v
GitHub Repository
    |
    v
Jenkins Pipeline
    |
    v
Docker Image Build
    |
    v
Docker Registry
    |
    v
Kubernetes Deployment
    |
    v
Running Application
```

---

## 📈 Kubernetes Components

* Deployment
* Service
* Horizontal Pod Autoscaler (HPA)
* Configurations for scalable deployment

---

## 🎯 Project Objectives

* Automate attendance tracking
* Improve attendance accuracy
* Reduce manual effort
* Enable scalable cloud-native deployment
* Demonstrate DevOps and MLOps practices

---

## 🔮 Future Enhancements

* AWS EKS Deployment
* Prometheus Monitoring
* Grafana Dashboards
* Multi-Campus Support
* Role-Based Access Control (RBAC)
* Attendance Analytics Dashboard





# 🏫 School CCTV Video Analytics System

A comprehensive, intelligent CCTV video analytics system designed for school premises. This system integrates real-time face recognition, student-guardian pairing validation, and automated WhatsApp alerts to enhance campus security.

## 📁 Repository Structure

This is a monorepo containing both the backend analytics engine and the frontend monitoring dashboard.

- **[`backend/`](backend/)**: FastAPI-based analytics engine using DeepFace and OpenCV for face recognition and Twilio for WhatsApp alerts.
- **[`frontend/`](frontend/)**: Next.js-based web interface for real-time monitoring and administrative management.
- **[`docs/`](docs/)**: Project documentation and requirements.

---

## 🚀 Quick Start

### 1. Backend Setup
Navigate to the `backend/` directory and follow the instructions in its [README](backend/README.md).
```bash
cd backend
pip install -r requirements.txt
uvicorn src.api.main:app --reload
```

### 2. Frontend Setup
Navigate to the `frontend/` directory and follow the instructions in its [README](frontend/README.md).
```bash
cd frontend
npm install
npm run dev
```

---

## 🛠️ Tech Stack

- **Computer Vision**: DeepFace, OpenCV
- **Backend**: FastAPI, SQLAlchemy, MySQL
- **Frontend**: Next.js, React, Tailwind CSS
- **Alerts**: Twilio (WhatsApp Business API)
- **Monitoring**: Streamlit (integrated in backend for rapid prototyping)

---

## 📈 Key Features

- **Real-time Identification**: Instant recognition of students, staff, and authorized guardians.
- **Stranger Alerts**: Immediate notifications when unknown individuals are detected in sensitive areas.
- **Pairing Validation**: Intelligent logic to ensure students leave only with registered guardians.
- **Scalable Architecture**: Designed to handle multiple camera feeds across a campus.

---

## 📄 Documentation

Detailed requirements and system design can be found in the [`docs/`](docs/) folder.

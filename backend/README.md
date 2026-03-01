# 🏫 School CCTV Video Analytics System

An intelligent CCTV video analytics system for school premises that uses face recognition to identify individuals, validate student-guardian relationships, detect strangers, and send instant WhatsApp alerts to security teams.

---

## 🚀 Features

- **Real-time Face Recognition** – Detects and identifies students, staff, and parents from live CCTV feeds
- **Stranger Detection** – Alerts when an unregistered person enters school premises
- **Student-Guardian Pairing Validation** – Flags suspicious pairings (student with unknown adult)
- **Instant WhatsApp Alerts** – Sends snapshots and alerts via Twilio to security personnel
- **Admin Dashboard** – Streamlit-based web UI for monitoring and managing face profiles
- **REST API** – FastAPI backend for programmatic access

---

## 🗂️ Project Structure

```
school-cctv-analytics/
├── src/
│   ├── api/           # FastAPI REST endpoints
│   ├── alerts/        # WhatsApp alert system (Twilio)
│   ├── dashboard/     # Streamlit monitoring dashboard
│   ├── detection/     # Face detection module
│   ├── recognition/   # Face recognition & matching
│   ├── decision/      # Alert decision logic
│   ├── ingestion/     # Video/camera feed ingestion
│   ├── preprocessing/ # Frame preprocessing
│   ├── config/        # Configuration management
│   └── utils/         # Utility helpers
├── database/          # SQL scripts & DB connection
├── scripts/           # Utility scripts
├── docs/              # Documentation
├── data/              # Videos, frames, face embeddings (gitignored)
├── requirements.txt
└── .env               # Environment variables (gitignored)
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Kanimozhi-28/School-CCTV-Video-Analytics-System.git
cd School-CCTV-Video-Analytics-System
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root:
```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=school_cctv
DB_USER=root
DB_PASSWORD=yourpassword
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
ALERT_TO_NUMBER=whatsapp:+91XXXXXXXXXX
```

---

## ▶️ Running the Application

### Start the API Server
```bash
uvicorn src.api.main:app --reload
```

### Start the Dashboard
```bash
streamlit run src/dashboard/streamlit_app.py
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Face Recognition | DeepFace, OpenCV |
| Backend API | FastAPI, Uvicorn |
| Dashboard | Streamlit |
| Database | MySQL (SQLAlchemy + PyMySQL) |
| Alerts | Twilio (WhatsApp) |
| Language | Python 3.10+ |

---

## 📋 Requirements

See [`requirements.txt`](requirements.txt) for the full list of dependencies.

---

## 📄 License

This project is for educational and security research purposes.

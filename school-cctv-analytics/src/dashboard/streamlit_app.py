
import streamlit as st
import cv2
import numpy as np
import os
import json
import face_recognition
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.recognition.face_embedder import FaceEmbedder
from src.recognition.similarity import find_best_match
from src.decision.pairing_logic import validate_pairing
from src.alerts.whatsapp_alert import send_whatsapp_alert

st.set_page_config(page_title="School CCTV Analytics", page_icon="🏫", layout="wide")

st.title("🏫 School CCTV Video Analytics")
st.markdown("---")

# Load embeddings
def load_embeddings(filepath):
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r") as f:
        return json.load(f)

# Load Databases
def get_databases():
    students = load_embeddings("data/embeddings/students.json")
    parents = load_embeddings("data/embeddings/parents.json")
    
    combined_db = {}
    roles = {}
    
    for face_id, vector in students.items():
        combined_db[face_id] = vector
        roles[face_id] = "Student"
        
    for face_id, vector in parents.items():
        combined_db[face_id] = vector
        roles[face_id] = "Parent"
        
    return combined_db, roles

# Student-Parent Relationships
relationships = {
    "1": "image1", "2": "image2"
}

# Name Mapping
name_mapping = {
    "1": "Aarav Sharma", "2": "Vivaan Gupta", "3": "Ananya Rao", "5": "Ishaan Singh",
    "6": "Sia Patel", "7": "Reyansh Das", "8": "Myra Jain", "10": "Kabir Verma", "11": "Zoya Khan",
    "image1": "Vikram Sharma", "image2": "Meera Gupta"
}

if st.sidebar.button("🔄 Refresh Face Database"):
    st.cache_data.clear()
    st.sidebar.success("Database refreshed!")

combined_db, roles = get_databases()
st.sidebar.info(f"Loaded {len(combined_db)} face profiles.")
confidence_threshold = st.sidebar.slider("Match Tolerance (Lower = Stricter)", 0.0, 1.0, 0.6, 0.05)

st.subheader("Upload CCTV Footage")
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Save video locally
    video_path = "uploaded_video.mp4"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    
    st.write(f"Source Width: {width}px | Total Frames: {total_frames}")
    
    # Optimization settings
    if width < 640:
        RESIZE_FACTOR = 1.0
        SKIP_FRAMES = 3
    else:
        RESIZE_FACTOR = 0.5
        SKIP_FRAMES = 5
        
    status_bar = st.progress(0)
    status_text = st.empty()
    stframe = st.empty()
    
    if st.button("Stop Processing"):
        st.write("Processing stopped.")
        cap.release()
    else:
        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_count += 1
            if frame_count % SKIP_FRAMES != 0:
                continue
            
            progress = min(frame_count / total_frames, 1.0)
            status_bar.progress(progress)
            
            if RESIZE_FACTOR != 1.0:
                small_frame = cv2.resize(frame, (0, 0), fx=RESIZE_FACTOR, fy=RESIZE_FACTOR)
            else:
                small_frame = frame
                
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            
            upsample = 1 if width < 640 else 0
            face_locations = face_recognition.face_locations(rgb_small_frame, number_of_times_to_upsample=upsample)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            
            detected_faces = []
            annotated_frame = rgb_small_frame.copy()
            
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                name, distance = find_best_match(face_encoding, combined_db, threshold=confidence_threshold)
                role = roles.get(name, "Unknown")
                detected_faces.append({'name': name, 'role': role})
                
                real_name = name_mapping.get(name, name)
                
                if role == "Student":
                    continue
                    
                color = (0, 0, 255) if role == "Parent" else (255, 0, 0)
                cv2.rectangle(annotated_frame, (left, top), (right, bottom), color, 2)
                label = f"{real_name} ({distance:.2f})"
                cv2.putText(annotated_frame, label, (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)

            # Pairing logic
            status, alerts = validate_pairing(detected_faces, relationships)
            
            # Show status
            if status == "SAFE":
                status_text.success(f"STATUS: {status}")
            elif status == "SUSPICIOUS":
                status_text.warning(f"STATUS: {status}!")
                for a in alerts:
                    send_whatsapp_alert(a)
            else:
                status_text.error(f"STATUS: {status}!")
                for a in alerts:
                    send_whatsapp_alert(a)

            stframe.image(annotated_frame, channels="RGB", use_container_width=True)
            
        cap.release()
else:
    st.info("Upload a video to start.")

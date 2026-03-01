
import cv2
import json
import os
import sys
import face_recognition
import numpy as np

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.recognition.similarity import find_best_match

def load_embeddings(embedding_file):
    if not os.path.exists(embedding_file):
        return {}
    with open(embedding_file, 'r') as f:
        return json.load(f)

def debug_recognition(video_path, output_dir="data/frames/extracted"):
    print(f"Starting diagnosis on: {video_path}")
    os.makedirs(output_dir, exist_ok=True)
    
    # Load known databases
    students_db = load_embeddings("data/embeddings/students.json")
    parents_db = load_embeddings("data/embeddings/parents.json")
    
    combined_db = {}
    roles = {}
    
    for name, vector in students_db.items():
        combined_db[name] = vector
        roles[name] = "Student"
    for name, vector in parents_db.items():
        combined_db[name] = vector
        roles[name] = "Parent"

    print(f"Loaded {len(combined_db)} total reference faces.")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Unable to open video {video_path}")
        return

    frame_count = 0
    # Process first 50 frames, saving every 10th
    while frame_count < 100:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        if frame_count % 20 != 0:
            continue

        print(f"Processing frame {frame_count}...")
        
        # We'll test different detection settings here
        # 1. Standard resize
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        # Detection
        # Try both upsampling and model types if needed
        face_locations = face_recognition.face_locations(rgb_small_frame, number_of_times_to_upsample=1)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        print(f"  Found {len(face_locations)} faces.")
        
        annotated_frame = frame.copy()
        
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Scale back up (since we detected on 0.5x size)
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2
            
            # Match
            name, distance = find_best_match(face_encoding, combined_db, threshold=0.6)
            role = roles.get(name, "Unknown")
            
            print(f"  - Detected: {name} ({role}) | Distance: {distance:.4f}")
            
            color = (0, 255, 0) if role == "Student" else (255, 0, 0)
            if name == "Unknown":
                color = (0, 0, 255)
            
            cv2.rectangle(annotated_frame, (left, top), (right, bottom), color, 2)
            label = f"{name} ({distance:.2f})"
            cv2.putText(annotated_frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        # Save frame
        out_path = os.path.join(output_dir, f"debug_frame_{frame_count}.jpg")
        cv2.imwrite(out_path, annotated_frame)
        print(f"  Saved diagnostic frame to: {out_path}")

    cap.release()
    print("Diagnosis complete.")

if __name__ == "__main__":
    # Check if uploaded_video.mp4 exists, or use the one in data/videos
    video_path = os.path.abspath("uploaded_video.mp4")
    if not os.path.exists(video_path):
        video_dir = "data/videos"
        vids = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
        if vids:
            video_path = os.path.join(video_dir, vids[0])
        else:
            print("No video found for diagnosis.")
            sys.exit(1)
            
    debug_recognition(video_path)

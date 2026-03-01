
import cv2
import json
import os
import sys
import face_recognition
import numpy as np

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ingestion.video_loader import VideoLoader
from src.recognition.similarity import find_best_match

def load_embeddings(embedding_file):
    if not os.path.exists(embedding_file):
        return {}
    with open(embedding_file, 'r') as f:
        return json.load(f)

def process_video(video_path, output_path=None):
    print(f"Processing video: {video_path}")
    
    # Load known databases
    students_db = load_embeddings("data/embeddings/students.json")
    parents_db = load_embeddings("data/embeddings/parents.json")
    
    # Combine databases for detection (tagging role)
    combined_db = {}
    roles = {} # name -> role
    
    for name, vector in students_db.items():
        combined_db[name] = vector
        roles[name] = "Student"
        
    for name, vector in parents_db.items():
        combined_db[name] = vector
        roles[name] = "Parent"

    loader = VideoLoader(video_path)
    
    # Prepare video writer if output path is provided
    writer = None
    
    frame_count = 0
    
    try:
        for frame in loader.stream_frames():
            frame_count += 1
            # Process every 2nd or 3rd frame for speed? Let's do every frame for now or optimize later
            
            # Resize for faster processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            # Convert BGR to RGB
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            
            # Detect faces
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # Scale back up
                top *= 2
                right *= 2
                bottom *= 2
                left *= 2
                
                name, distance = find_best_match(face_encoding, combined_db)
                role = roles.get(name, "Unknown")
                
                # Draw box
                color = (0, 255, 0) if role == "Student" else (255, 0, 0) # Green for student, Blue for parent
                if name == "Unknown":
                    color = (0, 0, 255) # Red for unknown
                    
                cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                
                # Draw label
                label = f"{name} ({role})"
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
                cv2.putText(frame, label, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)

            # Show frame
            cv2.imshow('Video Analytics', frame)
            
            # Write frame
            if output_path:
                if writer is None:
                    h, w = frame.shape[:2]
                    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                    writer = cv2.VideoWriter(output_path, fourcc, 20.0, (w, h))
                writer.write(frame)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except Exception as e:
        print(f"Error processing video: {e}")
    finally:
        loader.release()
        if writer:
            writer.release()
        cv2.destroyAllWindows()
        print("Processing complete.")

if __name__ == "__main__":
    video_dir = "data/videos"
    # Prioritize child video if it exists
    child_video = os.path.join(video_dir, "child video.mp4")
    
    if os.path.exists(child_video):
        target_video = child_video
        process_video(target_video)
    else:
        video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
        if video_files:
            target_video = os.path.join(video_dir, video_files[0])
            process_video(target_video)
        else:
            print("No video found in data/videos")


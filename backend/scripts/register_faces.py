import os
import json
import sys

# Add project root to path to allow imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.recognition.face_embedder import FaceEmbedder

def register_faces(base_dir, output_file):
    print(f"Scanning directory: {base_dir}")
    
    embedder = FaceEmbedder()
    embeddings = {}
    
    if not os.path.exists(base_dir):
        print(f"Directory not found: {base_dir}")
        return

    for filename in os.listdir(base_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(base_dir, filename)
            name = os.path.splitext(filename)[0]
            
            print(f"  Processing {filename}...", end=" ", flush=True)
            try:
                vector = embedder.get_embedding(image_path)
                if vector:
                    embeddings[name] = vector
                    print(f"DONE (vector size: {len(vector)})")
                else:
                    print("FAILED (No face detected)")
            except Exception as e:
                print(f"ERROR: {e}")
    
    # Save to JSON
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(embeddings, f)
    
    print(f"--- Completed {base_dir}. Saved {len(embeddings)} profiles to {output_file} ---\n")



if __name__ == "__main__":
    # Register Students
    print("--- Registering Students ---")
    register_faces(
        "data/faces/students", 
        "data/embeddings/students.json"
    )
    
    # Register Parents
    print("\n--- Registering Parents ---")
    register_faces(
        "data/faces/parents", 
        "data/embeddings/parents.json"
    )

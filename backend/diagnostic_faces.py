
import face_recognition
import os

def test_dir(d):
    print(f"Testing directory: {d}")
    if not os.path.exists(d):
        print("  Not found")
        return
    for f in os.listdir(d):
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            p = os.path.join(d, f)
            print(f"  Testing {f}...", end=" ")
            try:
                img = face_recognition.load_image_file(p)
                locs = face_recognition.face_locations(img)
                print(f"Found {len(locs)} faces")
            except Exception as e:
                print(f"Error: {e}")

test_dir("data/faces/students")
test_dir("data/faces/parents")

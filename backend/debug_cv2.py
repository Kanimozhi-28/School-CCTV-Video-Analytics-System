
import cv2
import os

video_path = "uploaded_video.mp4"
print(f"Testing video path: {os.path.abspath(video_path)}")
print(f"File exists: {os.path.exists(video_path)}")

cap = cv2.VideoCapture(video_path)
print(f"Capture Opened: {cap.isOpened()}")

if cap.isOpened():
    ret, frame = cap.read()
    print(f"Read Frame: {ret}")
    if ret:
        print(f"Frame Shape: {frame.shape}")
    else:
        print("Failed to read first frame")
else:
    print("Failed to open capture")
    # print debug info
    print(cv2.getBuildInformation())

cap.release()

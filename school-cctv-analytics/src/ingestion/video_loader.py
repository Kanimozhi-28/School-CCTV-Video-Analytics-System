import cv2
import os

class VideoLoader:
    def __init__(self, source):
        self.source = source
        if not os.path.exists(source) and not str(source).isdigit():
             raise ValueError(f"Video source not found: {source}")
        self.cap = cv2.VideoCapture(source)

    def get_frame(self):
        """Returns a single frame, or None if end of video"""
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def stream_frames(self):
        """Generator that yields frames until video ends"""
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            yield frame

    def release(self):
        self.cap.release()


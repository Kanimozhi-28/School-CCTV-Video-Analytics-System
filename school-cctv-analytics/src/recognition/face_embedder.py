import face_recognition
import cv2
import numpy as np
import os

class FaceEmbedder:
    def __init__(self, model_path=None):
        # face_recognition uses dlib models by default, path management is handled internally usually
        pass

    def get_embedding(self, image_path):
        """Loads an image and returns a 128-d face encoding as a list."""
        try:
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            
            if encodings:
                return encodings[0].tolist()
            return None
        except Exception as e:
            print(f"Error processing {image_path}: {str(e)}")
            return None

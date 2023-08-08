import cv2
from library.faceDetector.main import FaceDetector

class CascadeFaceDetector(FaceDetector):
    def __init__(self):
        self.model = None
    def load_model(self):
        self.model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    def detect_face(self, frame):
        return self.model.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
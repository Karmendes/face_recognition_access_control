from library.faceRecognition.main import FaceRecognitor
import face_recognition

class Recognitor(FaceRecognitor):
    def __init__(self,person_searcher):
        self.encodings = None
        self.person_searcher = person_searcher
    def get_encodings(self,frame):
        self.encodings = face_recognition.face_encodings(frame)
    def get_names(self,know_encodings):
        return self.person_searcher.search(self.encodings,know_encodings)
    def recognize_face(self,frame,know_encodings):
        self.get_encodings(frame)
        return self.get_names(know_encodings)
    

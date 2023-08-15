from library.faceRecognition.main import FaceRecognitor
import face_recognition

class Recognitor(FaceRecognitor):
    def __init__(self,person_searcher,know_encodings):
        self.encodings = None
        self.person_searcher = person_searcher
        self.know_encodings = know_encodings
    def get_encodings(self,frame):
        self.encodings = face_recognition.face_encodings(frame)
    def get_names(self):
        return self.person_searcher.search(self.encodings,self.know_encodings)
    def recognize_face(self,frame):
        self.get_encodings(frame)
        return self.get_names()
    

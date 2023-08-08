import cv2
from library.videoCapture.main import VideoCaptor


class CaptorOpenCV(VideoCaptor):
    def __init__(self,form = 0):
        self.camera = cv2.VideoCapture(form)
    def capture(self):
        return self.camera.read()

    def quit(self):
        self.camera.release()
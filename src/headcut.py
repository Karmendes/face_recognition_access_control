from library.pubSubConnect.main import PubSubConnect
from library.faceDetector.main import FaceDetector

class HeadCutter:
    def __init__(self,face_detector,pubsub_connector):
        self.detector = face_detector
        self.conenctor = pubsub_connector
    def run(self):
        while True:
            frame = self.conenctor.pull_msg
            frame_face = self.detector.detect_face(frame)
            if len(frame_face) > 0:
                self.conenctor.push_msg(frame_face)
            else:
                print('Face not detected')

if __name__ == '__main__':
    headcutter = HeadCutter(FaceDetector(),PubSubConnect())
    headcutter.run()
        
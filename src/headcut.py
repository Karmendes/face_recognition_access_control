from library.pubSubConnect.connector_rabbitmq import RabbitConnector
from library.faceDetector.cascade_detector import CascadeFaceDetector
from library.imageProcess.main import FrameProcessorToFaceDetector
from time import sleep

class HeadCutter:
    def __init__(self,face_detector,pubsub_connector,processor):
        self.detector = face_detector
        self.conenctor = pubsub_connector
        self.processor = processor
        self.detector.load_model()
    def run(self):
        while True:
            method_frame, _, body = self.conenctor.pull_msg()
            if body is None:
                print('Sem mensagens para processar')
                sleep(2)
                continue
            frame_processed = self.processor.run(body)
            frame_face = self.detector.detect_face(frame_processed)
            if len(frame_face) > 0:
                #self.conenctor.push_msg(frame_face)
                print('Face detected')
            else:
                print('Face not detected')
            self.conenctor.channel.basic_ack(delivery_tag=method_frame.delivery_tag)

if __name__ == '__main__':
    headcutter = HeadCutter(CascadeFaceDetector(),RabbitConnector(),FrameProcessorToFaceDetector())
    headcutter.run()
        
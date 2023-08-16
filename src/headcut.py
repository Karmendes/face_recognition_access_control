from library.pubSubConnect.connector_rabbitmq import RabbitConnector
from library.faceDetector.cascade_detector import CascadeFaceDetector
from library.imageProcess.main import FrameDecodeBGRToGray,FrameDecode,FrameEncode
from library.utils.main import biggest_area,crop_frame
from time import sleep

class HeadCutter:
    def __init__(self,face_detector,pre_processor,pos_processor,pos_pos_processor,pubsub_connector_receiver,pubsub_connector_sender):
        self.detector = face_detector
        self.connector_receiver = pubsub_connector_receiver
        self.pre_processor = pre_processor
        self.pos_processor = pos_processor
        self.pos_pos_processor = pos_pos_processor
        self.connector_sender = pubsub_connector_sender
        self.detector.load_model()
    def run(self):
        while True:
            # Receive the frame
            method_frame, _, body = self.connector_receiver.pull_msg()
            # Check if has something
            if body is None:
                continue
            # Process to detect face
            frame_processed = self.pre_processor.run(body)
            # Detect face
            landmarks_face = self.detector.detect_face(frame_processed)
            if len(landmarks_face) > 0:
                # Get the bigger face
                coord = biggest_area(landmarks_face)
                frame_face = self.pos_processor.run(body)
                frame_crop = crop_frame(frame_face,coord)
                # Send to queue
                frame_crop = self.pos_pos_processor.run(frame_crop)
                self.connector_sender.push_msg(frame_crop)
                print('Face detected')
            else:
                print('Face not detected')
            self.connector_receiver.channel.basic_ack(delivery_tag=method_frame.delivery_tag)

if __name__ == '__main__':
    headcutter = HeadCutter(CascadeFaceDetector(),
                            FrameDecodeBGRToGray(),
                            FrameDecode(),
                            FrameEncode(),
                            RabbitConnector(),
                            RabbitConnector(queue_name= 'HeadCut_to_FaceRecognition'))
    headcutter.run()
        
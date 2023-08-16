from library.pubSubConnect.connector_rabbitmq import RabbitConnector
from library.faceRecognition.ageitgey.face_recognition import Recognitor
from library.faceRecognition.ageitgey.searcher.comparer_faces import Comparer
from library.imageProcess.main import DecodeFrame,EncodeFrame
from library.utils.main import open_encodings
from library.logger.main import Logger

class Severiner:
    def __init__(self,connector_from,connector_to,recognitor,decoder,encoder):
        Logger.emit('Initializing severiner')
        self.connector_from = connector_from
        self.connector_to = connector_to
        self.recognitor = recognitor
        self.encoder = encoder
        self.decoder = decoder
        self.know_encodings = open_encodings()

    def run(self):
        while True:
            # Receive the frame
            method_frame, _, body = self.connector_from.pull_msg()
            # Decode the frame
            if body is None:
                continue
            # Decode Frame
            frame_face = self.decoder.process(body)
            # Recognize the face
            Logger.emit('Identifying face')
            name = self.recognitor.recognize_face(frame_face,self.know_encodings)
            # Send for pubsub
            if name != 'Unknown':
                Logger.emit(f'Sending {name} for queue')
                self.connector_to.push_msg(name)
            self.connector_from.channel.basic_ack(delivery_tag=method_frame.delivery_tag)

if __name__ == '__main__':
    severiner = Severiner(RabbitConnector(queue_name='HeadCut_to_FaceRecognition'),
                          RabbitConnector(queue_name='FaceRecognition_to_Concierge'),
                          Recognitor(Comparer()),
                          DecodeFrame(),
                          EncodeFrame())
    severiner.run()


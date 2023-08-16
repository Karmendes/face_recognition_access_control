from library.pubSubConnect.connector_rabbitmq import RabbitConnector
from library.faceRecognition.ageitgey.face_recognition import Recognitor
from library.faceRecognition.ageitgey.searcher.comparer_faces import Comparer
from library.imageProcess.main import FrameDecodeBGRToRGB
from library.utils.main import create_folder_if_not_exists,save_encodings,save_images

class Register:
    def __init__(self,connector_from,face_recognition,decorder,name):
        self.connector_from = connector_from
        self.recognitor = face_recognition
        self.decoder = decorder
        self.name = name
    
    def run(self):
        encodings = []
        names = []
        frames = []
        while True:
            # Receive the frame
            method_frame, _, body = self.connector_from.pull_msg()
            # Check if has something
            if body is None:
                break
            # Decode Frame
            print('Gerando encodings')
            frame_face = self.decoder.run(body)
            # Get encodings
            self.recognitor.get_encodings(frame_face)
            if len(self.recognitor.encodings) > 0:
                encodings.append(self.recognitor.encodings[0])
                names.append(self.name)
                frames.append(frame_face)
            self.connector_from.channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        if len(encodings) > 0:
            create_folder_if_not_exists(f'users/{self.name}')
            save_encodings(encodings,names,self.name)
            create_folder_if_not_exists(f'images/{self.name}')
            save_images(frames,self.name)

if __name__ == '__main__':
    register = Register(RabbitConnector(queue_name='HeadCut_to_FaceRecognition'),Recognitor(Comparer()),FrameDecodeBGRToRGB(),'Lucas_Mendes')
    register.run()
    
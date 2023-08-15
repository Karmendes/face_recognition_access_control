from library.pubSubConnect.connector_rabbitmq import RabbitConnector
from library.faceRecognition.ageitgey.face_recognition import Recognitor
from library.faceRecognition.ageitgey.searcher.comparer_faces import Comparer
from library.imageProcess.main import DecodeFrame
from library.utils.main import create_folder_if_not_exists,save_encodings

class Register:
    def __init__(self,connector_from,face_recognition,decorder,name):
        self.connector_from = connector_from
        self.recognitor = face_recognition
        self.decoder = decorder
        self.name = name
    
    def run(self):
        encodings = []
        names = []
        while True:
            # Receive the frame
            method_frame, _, body = self.connector_from.pull_msg()
            # Check if has something
            if body is None:
                break
            # Decode Frame
            frame_face = self.decoder.process(body)
            # Get encodings
            self.recognitor.get_encodings(frame_face)
            if len(self.recognitor.encodings) > 0:
                encodings.append(self.recognitor.encodings)
                names.append(self.name)
        create_folder_if_not_exists(f'src/users/{self.name}')
        save_encodings(encodings,names,self.name)

if __name__ == '__main__':
    register = Register(RabbitConnector(queue_name='HeadCut_to_FaceRecognition'),Recognitor(Comparer),DecodeFrame(),'Lucas_Mendes')
    register.run()
    
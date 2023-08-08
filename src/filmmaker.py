from library.videoCapture.opencv_capture import CaptorOpenCV
from library.imageProcess.main import FrameProcessorToFilmMaker
from library.pubSubConnect.connector_rabbitmq import RabbitConnector
from time import sleep


class FilmMaker:
    def __init__(self,video_capture,image_processor,connector):
        self.video_capture = video_capture
        self.image_processor = image_processor
        self.connector = connector

    def run(self):
        while True:
            try:
                _,frame = self.video_capture.capture()
                processed_frame = self.image_processor.run(frame)
                self.connector.push_msg(processed_frame)
                print('Frame enviado para fila')
                sleep(1)
            except KeyboardInterrupt:
                self.connector.close()
                self.video_capture.quit()
if __name__ == '__main__':
    maker = FilmMaker(CaptorOpenCV(),FrameProcessorToFilmMaker(),RabbitConnector())
    maker.run()
from library.videoCapture.opencv_capture import CaptorOpenCV
from library.imageProcess.main import FrameEncode
from library.pubSubConnect.connector_rabbitmq import RabbitConnector
from time import sleep
from library.logger.main import Logger


class FilmMaker:
    def __init__(self,video_capture,image_processor,connector):
        Logger.emit('Initializing filmaker')
        self.video_capture = video_capture
        self.image_processor = image_processor
        self.connector = connector

    def run(self):
        while True:
            try:
                Logger.emit('Capturing frame from feed camera')
                _,frame = self.video_capture.capture()
                processed_frame = self.image_processor.run(frame)
                self.connector.push_msg(processed_frame)
                Logger.emit('Frame sended for queue')
                sleep(1)
            except KeyboardInterrupt:
                self.connector.close()
                self.video_capture.quit()
                Logger.emit('Exiting...')
if __name__ == '__main__':
    maker = FilmMaker(CaptorOpenCV(),FrameEncode(),RabbitConnector())
    maker.run()
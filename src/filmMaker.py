from library.videoCapture.main import VideoCaptor
from library.imageProcess.main import ImageProcessor
from library.pubSubConnect.main import PubSubConnect


class FilmMaker:
    def __init__(self,video_capture,image_processor,connector):
        self.video_capture = video_capture
        self.image_processor = image_processor
        self.connector = connector

    def run(self):

        while True:
            try:## Grab the image
                frame = self.video_capture.capture_from_camera()
                processed_frame = self.image_processor.process_frame(frame)
                self.connector.push_msg(processed_frame)
            except:
                print('My Bad')
                break

if __name__ == '__main__':
    maker = FilmMaker(VideoCaptor(),ImageProcessor(),PubSubConnect())
    maker.run()
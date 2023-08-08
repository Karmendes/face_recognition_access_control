import cv2
import numpy as np

class FrameProcessorStrategy:
    def process(self, frame):
        pass

class BufferToArrayStrategy(FrameProcessorStrategy):
    def process(self, frame):
        return np.frombuffer(frame, dtype=np.uint8)

class ArrayToFrameStrategy(FrameProcessorStrategy):
    def process(self, frame):
        return cv2.imdecode(frame, cv2.IMREAD_COLOR)

class BGRToGray(FrameProcessorStrategy):
    def process(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

class FrameToBufferStrategy(FrameProcessorStrategy):
    def process(self, frame):
        _, buffer = cv2.imencode('.jpg', frame)
        return buffer

class BufferToBytesStrategy(FrameProcessorStrategy):
    def process(self, frame):
        return frame.tobytes()

class CropFrame(FrameProcessorStrategy):
    def __init__(self, coord):
        self.coord = coord
    def process(self, frame):
        X, Y, W, H = self.coord
        return frame[Y:Y+H, X:X+W]

class FrameProcessor:
    def __init__(self):
        self.strategies = []
    def add_strategy(self, strategy):
        self.strategies.append(strategy)
    def process_frame(self, frame):
        processed_frame = frame
        for strategy in self.strategies:
            processed_frame = strategy.process(processed_frame)
        return processed_frame

################################################################### directors

class FrameProcessorToFilmMaker:
    def __init__(self):
        self.frame_processor = FrameProcessor()
        self.frame_processor.add_strategy(FrameToBufferStrategy())
        self.frame_processor.add_strategy(BufferToBytesStrategy())
    def run(self,frame):
        return self.frame_processor.process_frame(frame)

class FrameProcessorToFaceDetector:
    def __init__(self):
        self.frame_processor = FrameProcessor()
        self.frame_processor.add_strategy(BufferToArrayStrategy())
        self.frame_processor.add_strategy(ArrayToFrameStrategy())
        self.frame_processor.add_strategy(BGRToGray())
    def run(self,frame):
        return self.frame_processor.process_frame(frame)
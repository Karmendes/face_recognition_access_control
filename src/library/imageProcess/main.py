import cv2

class FrameProcessorStrategy:
    def process(self, frame):
        pass

class FrameToBufferStrategy(FrameProcessorStrategy):
    def process(self, frame):
        _, buffer = cv2.imencode('.jpg', frame)
        return buffer

class BufferToBytesStrategy(FrameProcessorStrategy):
    def process(self, frame):
        return frame.tobytes()

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

class FrameProcessorToFilmMaker:
    def __init__(self):
        self.frame_processor = FrameProcessor()
        self.frame_processor.add_strategy(FrameToBufferStrategy())
        self.frame_processor.add_strategy(BufferToBytesStrategy())
    def run(self,frame):
        return self.frame_processor.process_frame(frame)
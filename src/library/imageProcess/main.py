import cv2
import numpy as np

# Interface

class FrameProcessorStrategy:
    def process(self, frame):
        pass


## Basic funtions

class BufferToArrayStrategy(FrameProcessorStrategy):
    def process(self, frame):
        return np.frombuffer(frame, dtype=np.uint8)

class ArrayToFrameStrategy(FrameProcessorStrategy):
    def process(self, frame):
        return cv2.imdecode(frame, cv2.IMREAD_COLOR)

class BGRToGray(FrameProcessorStrategy):
    def process(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

class GrayToBGR(FrameProcessorStrategy):
    def process(self, gray_frame):
        return cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

class GrayToRGB(FrameProcessorStrategy):
    def process(self, frame):
        return cv2.cvtColor(frame,cv2.COLOR_GRAY2RGB)

class BGRToRGB(FrameProcessorStrategy):
    def process(self, frame):
        return cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

class FrameToBufferStrategy(FrameProcessorStrategy):
    def process(self, frame):
        _, buffer = cv2.imencode('.jpg', frame)
        return buffer

class BufferToBytesStrategy(FrameProcessorStrategy):
    def process(self, frame):
        return frame.tobytes()


## Personalized functions

class EncodeFrame(FrameProcessorStrategy):
    def process(self, frame):
        frame = FrameToBufferStrategy().process(frame)
        return BufferToBytesStrategy().process(frame)

class DecodeFrame(FrameProcessorStrategy):
    def process(self, frame):
        frame = BufferToArrayStrategy().process(frame)
        return ArrayToFrameStrategy().process(frame)


## Aggregate Strategys

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


class FrameEncode:
    def __init__(self):
        self.frame_processor = FrameProcessor()
        self.frame_processor.add_strategy(EncodeFrame())
    def run(self,frame):
        return self.frame_processor.process_frame(frame)

class FrameDecode:
    def __init__(self):
        self.frame_processor = FrameProcessor()
        self.frame_processor.add_strategy(DecodeFrame())
    def run(self,frame):
        return self.frame_processor.process_frame(frame)

class FrameDecodeBGRToGray:
    def __init__(self):
        self.frame_processor = FrameProcessor()
        self.frame_processor.add_strategy(DecodeFrame())
        self.frame_processor.add_strategy(BGRToGray())
        
    def run(self,frame):
        return self.frame_processor.process_frame(frame)
    
class FrameGrayToBGREncode:
    def __init__(self):
        self.frame_processor = FrameProcessor()
        self.frame_processor.add_strategy(GrayToBGR())
        self.frame_processor.add_strategy(EncodeFrame())
    def run(self,frame):
        return self.frame_processor.process_frame(frame)
    
class FrameDecodeBGRToRGB:
    def __init__(self):
        self.frame_processor = FrameProcessor()
        self.frame_processor.add_strategy(DecodeFrame())
        self.frame_processor.add_strategy(BGRToRGB())
    def run(self,frame):
        return self.frame_processor.process_frame(frame)
    


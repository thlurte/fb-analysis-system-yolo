from ultralytics import YOLO
from interfaces.i_detector import IDetector

class YOLODetector(IDetector):
    def __init__(self, model_path: str, batch_size: int = 20, confidence: float = 0.1):
        self.model = YOLO(model=model_path)
        self.batch_size = batch_size
        self.confidence = confidence

    def detect(self, frames):
        detections = []
        for i in range(0, len(frames), self.batch_size):
            detections_batch = self.model.predict(frames[i:i+batch_size], conf=self.confidence)
            detections += detections_batch
        return detections 
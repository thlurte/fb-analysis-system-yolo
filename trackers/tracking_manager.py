import os
import pickle
from interfaces.i_detector import IDetector
from interfaces.i_object_tracker import IObjectTracker

class TrackingManager:
    def __init__(self, detector: IDetector, tracker: IObjectTracker):
        self.detector = detector
        self.tracker = tracker

    def get_object_tracks(self, frames, read_from_stub=False, stub_path=None):
        if read_from_stub and stub_path is not None and os.path.exists(stub_path):
            with open(stub_path, 'rb') as f:
                return pickle.load(f)
        
        detections = self.detector.detect(frames)
        tracks = self.tracker.track(detections)

        if stub_path is not None:
            with open(stub_path, 'wb') as f:
                pickle.dump(tracks, f)

        return tracks 
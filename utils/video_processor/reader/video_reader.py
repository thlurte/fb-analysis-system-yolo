import cv2
from interfaces.i_video_reader import IVideoReader
from typing import List

class VideoReader(IVideoReader):
    def __init__(self, video_path: str):
        self.video_path = video_path

    def read(self) -> List:
        cap = cv2.VideoCapture(self.video_path)
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
        return frames

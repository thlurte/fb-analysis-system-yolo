from video_processor import VideoProcessor
import cv2

class VideoReader(VideoProcessor):
    def __intit__(self, video_path: str):
        self.video_path = video_path

    def process(self):
        cap = cv2.VideoCapture(self.video_path)
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
        cap.release()
        return frames
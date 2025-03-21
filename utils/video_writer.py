import cv2
from video_processor import VideoProcessor

class VideoWriter(VideoProcessor):
    def __init__(self, output_path: str):
        self.output_path = output_path

    def process(self, video_frames):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(self.output_path, fourcc, 24, (video_frames[0].shape[1],video_frames[0].shape[0]))
        for frame in video_frames:
            out.write(frame)
        out.release()


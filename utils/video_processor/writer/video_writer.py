import cv2
from interfaces.i_video_writer import IVideoWriter
from typing import List

class VideoWriter(IVideoWriter):
    def __init__(self, output_path: str):
        self.output_path = output_path

    def write(self, video_frames: List):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(self.output_path, fourcc, 24, (video_frames[0].shape[1], video_frames[0].shape[0]))
        for frame in video_frames:
            out.write(frame)
        out.release()

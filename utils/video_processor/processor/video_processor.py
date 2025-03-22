from interfaces.i_video_reader import IVideoReader
from interfaces.i_video_writer import IVideoWriter
from typing import List

class VideoProcessor:
    def __init__(self, reader: IVideoReader, writer: IVideoWriter):
        self.reader = reader
        self.writer = writer

    def process_video(self):
        frames = self.reader.read()
        self.writer.write(frames)

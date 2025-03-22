from utils.video_processor.processor.video_processor import VideoProcessor
from utils.video_processor.reader.video_reader import VideoReader
from utils.video_processor.writer.video_writer import VideoWriter

def main():
    # read video frames
    reader = VideoReader('input_videos/08fd33_4.mp4')
    writer = VideoWriter('output_videos/08fd33_4.avi')

    # inference

    # tracking

    # write frames into a video
    # writer = VideoWriter('output_videos/08fd33_4.avi')
    # writer.process(frames)
    video_processor = VideoProcessor(reader, writer)
    video_processor.process_video()

if __name__ == '__main__':
    main()

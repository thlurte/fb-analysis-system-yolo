from utils.video_reader import VideoReader
from utils.video_writer import VideoWriter


def main():
    # read video frames
    reader = VideoReader('input_videos/08fd33_4.mp4')
    frames = reader.process()

    # inference

    # tracking

    # write frames into a video
    writer = VideoWriter('output_videos/08fd33_4.avi')
    writer.process(frames)

if __name__ == '__main__':
    main()

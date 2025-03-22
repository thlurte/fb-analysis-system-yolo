from utils.video_processor.processor.video_processor import VideoProcessor
from utils.video_processor.reader.video_reader import VideoReader
from utils.video_processor.writer.video_writer import VideoWriter
from trackers.yolo_detector import YOLODetector
from trackers.byte_tracker import ByteTracker
from trackers.tracking_manager import TrackingManager

def main():
    # read video frames
    reader = VideoReader('input_videos/08fd33_4.mp4')
    writer = VideoWriter('output_videos/08fd33_4.avi')

    # tracking
    detector = YOLODetector('models/best.pt')
    tracker = ByteTracker()
    tracking_manager = TrackingManager(detector, tracker)

    tracks = tracking_manager.get_object_tracks(
        reader.read(),
        read_from_stub=True,
        stub_path='stubs/track_stubs.pkl'
    )

    # write frames into a video
    video_processor = VideoProcessor(reader, writer)
    video_processor.process_video()

if __name__ == '__main__':
    main()

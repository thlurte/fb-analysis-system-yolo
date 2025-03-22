from abc import ABC, abstractmethod

class IVideoWriter(ABC):
    @abstractmethod
    def write(self,video_frames):
        pass
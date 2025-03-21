from abc import ABC,abstractmethod

class VideoProcessor(ABC):
    @abstractmethod
    def process(self):
        pass

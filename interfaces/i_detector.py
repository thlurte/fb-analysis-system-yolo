from abc import ABC, abstractmethod
from typing import List

class IDetector(ABC):
    @abstractmethod
    def detect(self, frames: List) -> List:
        pass 
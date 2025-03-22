from abc import ABC, abstractmethod
from typing import List, Dict

class IObjectTracker(ABC):
    @abstractmethod
    def track(self, detections: List) -> Dict:
        pass 
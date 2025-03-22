from abc import ABC, abstractmethod
from typing import List

class IVideoReader(ABC):
    @abstractmethod
    def read(self) -> List:
        pass
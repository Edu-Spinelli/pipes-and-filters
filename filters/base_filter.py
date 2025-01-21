# log_processor/filters/base_filter.py
from abc import ABC, abstractmethod

class BaseFilter(ABC):
    @abstractmethod
    def process(self, data):
        pass

# log_processor/filters/group_filter.py
from collections import Counter
from .base_filter import BaseFilter

class GroupFilter(BaseFilter):
    def process(self, data):
        grouped = Counter(log["message"] for log in data)
        return [{"message": key, "count": value} for key, value in grouped.items()]

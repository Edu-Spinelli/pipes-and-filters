# log_processor/pipe.py
class Pipe:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter_instance):
        self.filters.append(filter_instance)

    def process(self, data):
        for filter_instance in self.filters:
            data = filter_instance.process(data)
        return data

from .base_filter import BaseFilter

class ErrorFilter(BaseFilter):
    def process(self, data):
        """
        Filtra apenas os logs de nível ERROR.
        :param data: Lista de dicionários representando os logs.
        :return: Lista contendo apenas os logs com nível ERROR.
        """
        return [log for log in data if log["level"] == "ERROR"]

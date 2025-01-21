from .base_filter import BaseFilter

class InfoFilter(BaseFilter):
    def process(self, data):
        """
        Filtra apenas os logs de nível INFO.
        :param data: Lista de dicionários representando os logs.
        :return: Lista contendo apenas os logs com nível INFO.
        """
        return [log for log in data if log["level"] == "INFO"]

from .base_filter import BaseFilter

class WarningFilter(BaseFilter):
    def process(self, data):
        """
        Filtra apenas os logs de nível WARNING.
        :param data: Lista de dicionários representando os logs.
        :return: Lista contendo apenas os logs com nível WARNING.
        """
        return [log for log in data if log["level"] == "WARNING"]

# log_processor/filters/grouped_export_filter.py
from .base_filter import BaseFilter
import csv

class GroupedExportFilter(BaseFilter):
    def __init__(self, output_file):
        """
        Inicializa o filtro de exportação para dados agrupados.
        :param output_file: Caminho do arquivo de saída.
        """
        self.output_file = output_file

    def process(self, data):
        """
        Exporta dados agrupados para um arquivo CSV.
        :param data: Lista de dicionários representando os logs agrupados.
        :return: Os dados sem modificações.
        """
        with open(self.output_file, "w", newline="") as file:
            fieldnames = ["message", "count"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return data

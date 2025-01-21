# log_processor/filters/export_filter.py
from .base_filter import BaseFilter
import csv

class ExportFilter(BaseFilter):
    def __init__(self, output_file_base="logs/report"):
        """
        Inicializa o filtro de exportação.
        :param output_file_base: Base para os nomes dos arquivos de exportação.
        """
        self.output_file_base = output_file_base

    def process(self, data):
        """
        Processa os dados e exporta para arquivos CSV separados por nível de log.
        :param data: Lista de dicionários representando os logs processados.
        """
        # Separar os logs por nível
        categorized_logs = {"INFO": [], "WARNING": [], "ERROR": []}
        for log in data:
            if log["level"] in categorized_logs:
                categorized_logs[log["level"]].append(log)

        # Exportar logs categorizados
        for level, logs in categorized_logs.items():
            if logs:  # Exportar somente se houver logs para o nível
                file_name = f"{self.output_file_base}_{level.lower()}.csv"
                self._export_to_csv(file_name, logs)

        return data  # Retorna os dados sem modificá-los

    def _export_to_csv(self, file_name, logs):
        """
        Exporta uma lista de logs para um arquivo CSV.
        :param file_name: Nome do arquivo de saída.
        :param logs: Lista de logs a serem exportados.
        """
        with open(file_name, "w", newline="") as file:
            fieldnames = ["timestamp", "level", "message"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(logs)

# log_processor/main.py
from pipe import Pipe
from filters.parse_filter import ParseFilter
from filters.error_filter import ErrorFilter
from filters.warning_filter import WarningFilter
from filters.info_filter import InfoFilter
from filters.group_filter import GroupFilter
from filters.grouped_export_filter import GroupedExportFilter

if __name__ == "__main__":
    # Ler logs do arquivo
    with open("logs/server.log", "r") as log_file:
        raw_logs = log_file.read()

    # Pipeline para filtrar, agrupar e exportar erros
    error_pipeline = Pipe()
    error_pipeline.add_filter(ParseFilter())
    error_pipeline.add_filter(ErrorFilter())  # Filtra apenas erros
    error_pipeline.add_filter(GroupFilter())  # Agrupa os erros
    error_pipeline.add_filter(GroupedExportFilter(output_file="logs/grouped_errors_report.csv"))

    # Pipeline para filtrar, agrupar e exportar warnings
    warning_pipeline = Pipe()
    warning_pipeline.add_filter(ParseFilter())
    warning_pipeline.add_filter(WarningFilter())  # Filtra apenas warnings
    warning_pipeline.add_filter(GroupFilter())  # Agrupa os warnings
    warning_pipeline.add_filter(GroupedExportFilter(output_file="logs/grouped_warnings_report.csv"))

    # Pipeline para filtrar, agrupar e exportar infos
    info_pipeline = Pipe()
    info_pipeline.add_filter(ParseFilter())
    info_pipeline.add_filter(InfoFilter())  # Filtra apenas infos
    info_pipeline.add_filter(GroupFilter())  # Agrupa as infos
    info_pipeline.add_filter(GroupedExportFilter(output_file="logs/grouped_infos_report.csv"))

    # Processar os pipelines
    print("Processando logs agrupados de ERROR...")
    error_pipeline.process(raw_logs)
    print("Logs de ERROR agrupados exportados para logs/grouped_errors_report.csv")

    print("Processando logs agrupados de WARNING...")
    warning_pipeline.process(raw_logs)
    print("Logs de WARNING agrupados exportados para logs/grouped_warnings_report.csv")

    print("Processando logs agrupados de INFO...")
    info_pipeline.process(raw_logs)
    print("Logs de INFO agrupados exportados para logs/grouped_infos_report.csv")

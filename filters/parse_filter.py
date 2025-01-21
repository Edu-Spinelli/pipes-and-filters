from .base_filter import BaseFilter
class ParseFilter(BaseFilter):
    def process(self, data):
        """
        Transforma logs brutos em uma lista de dicionários estruturados.
        :param data: Dados brutos de log em formato de string.
        :return: Lista de dicionários estruturados.
        """
        parsed_logs = []
        for line in data.split("\n"):
            if line.strip():  # Ignorar linhas vazias
                parts = line.split(" - ")
                if len(parts) >= 3:  # Garantir que a linha está no formato esperado
                    parsed_logs.append({
                        "timestamp": parts[0].strip(),
                        "level": parts[1].strip(),
                        "message": parts[2].strip(),
                    })
        return parsed_logs

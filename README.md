# Trabalho ATA2 - Sistema Pipes and Filters

Este repositório contém a implementação de um sistema baseado no padrão arquitetural **Pipes and Filters** para processamento, filtragem, agrupamento e exportação de logs.

---

## **Descrição do Sistema**

O sistema foi projetado para processar grandes volumes de logs gerados por sistemas computacionais. Ele é capaz de:

- Estruturar logs brutos.
- Filtrar logs por níveis específicos: **ERROR**, **WARNING**, e **INFO**.
- Agrupar logs por mensagens idênticas e contar a frequência.
- Exportar relatórios organizados no formato CSV para análise.

---

## **Estrutura do Projeto**

```plaintext
├── filters/             # Contém os filtros usados no padrão Pipes and Filters
│   ├── base_filter.py           # Classe abstrata que define o contrato para os filtros
│   ├── parse_filter.py          # Filtra e estrutura logs brutos
│   ├── error_filter.py          # Filtra logs do nível ERROR
│   ├── warning_filter.py        # Filtra logs do nível WARNING
│   ├── info_filter.py           # Filtra logs do nível INFO
│   ├── group_filter.py          # Agrupa logs e conta a frequência
│   └── grouped_export_filter.py # Exporta logs agrupados em formato CSV
├── logs/               # Contém os arquivos de log e resultados exportados
├── main.py             # Ponto de entrada do sistema
├── pipe.py             # Classe que gerencia o fluxo de dados entre os filtros
└── README.md           # Documentação do projeto
```

---

## **Tecnologias Utilizadas**
- **Python 3.8+**
- Bibliotecas padrão:
  - `abc`: Para criação de classes abstratas.
  - `csv`: Para exportação dos dados agrupados em formato CSV.
  - `collections.Counter`: Para contagem eficiente de elementos.

---

## **Como Funciona?**

O sistema utiliza o padrão **Pipes and Filters**, onde cada filtro realiza uma transformação ou filtragem específica nos dados. O pipeline é gerenciado pela classe `Pipe`, que passa os dados por cada filtro de forma sequencial.

### **Fluxo Geral**
1. O arquivo de logs brutos é lido e enviado ao pipeline.
2. Os dados passam pelos seguintes filtros:
   - **ParseFilter**: Converte os logs brutos em uma estrutura organizada.
   - **Filtros Específicos** (`ErrorFilter`, `WarningFilter`, `InfoFilter`): Filtram logs por nível.
   - **GroupFilter**: Agrupa os logs por mensagem e conta a frequência.
   - **GroupedExportFilter**: Exporta os dados agrupados para arquivos CSV.
3. O pipeline exporta relatórios organizados no diretório `logs/`.

---

## **Como Executar?**

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/Edu-Spinelli/pipes-and-filters.git
   cd Trabalho_ATA2
   ```

2. **Certifique-se de ter o Python instalado**:
   ```bash
   python --version
   ```

3. **Crie ou insira um arquivo de log no diretório `logs/`**:
   - Exemplo de log no arquivo `server.log`:
     ```plaintext
     2025-01-20 12:00:00 - INFO - Server started
     2025-01-20 12:01:00 - ERROR - Database connection failed
     2025-01-20 12:02:00 - WARNING - Disk space low
     ```

4. **Execute o Sistema**:
   ```bash
   python main.py
   ```

5. **Verifique os Arquivos Gerados**:
   - Relatórios CSV gerados no diretório `logs/`:
     - `grouped_errors_report.csv`
     - `grouped_warnings_report.csv`
     - `grouped_infos_report.csv`

---

## **Exemplo de Arquivo de Log**
```plaintext
2025-01-20 12:00:00 - INFO - Server started
2025-01-20 12:01:00 - ERROR - Database connection failed
2025-01-20 12:02:00 - WARNING - Disk space low
2025-01-20 12:03:00 - ERROR - Timeout while connecting to service
2025-01-20 12:04:00 - INFO - User logged in
```

---

## **Relatórios Gerados**
### **Exemplo: `grouped_errors_report.csv`**
```csv
message,count
Database connection failed,2
Timeout while connecting to service,1
```

### **Exemplo: `grouped_warnings_report.csv`**
```csv
message,count
Disk space low,1
```

### **Exemplo: `grouped_infos_report.csv`**
```csv
message,count
Server started,1
User logged in,1
```

---

## **Autores**
- **Eduardo Spinelli**

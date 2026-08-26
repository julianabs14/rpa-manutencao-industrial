import logging
import os
from datetime import datetime
from src.config import PASTA_LOGS

def configurar_logger():
    os.makerdirs(PASTA_LOGS, exist_ok=True)

    nome_arquivo = datetime.now().strftime("%Y-%m-%d") + ".log"
    caminho_log = os.path.join(PASTA_LOGS, nome_arquivo)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(message)s",
        handlers=[
            logging.FileHandler(caminho_log, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger("rpa_manutencao")
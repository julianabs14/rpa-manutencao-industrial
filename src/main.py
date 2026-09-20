import time
from src.logger_setup import configurar_logger
from src.processor import carregar_dados, limpar_dados, calcular_kpis
from src.report_builder import gerar_relatorio_excel
from src.emailer import enviar_relatorio_por_email

logger = configurar_logger()

def montar_resumo_texto(resumo_df):
    linhas = []
    for _, linha in resumo_df.iterrows():
        marcador = "[CRITICO] " if linha["critico"] else ""
        linhas.append(
            f"{marcador}{linha["equipamento"]}: "
            f"{linha["total_paradas"]} paradas, "
            f"media de {linha["duracao_media_minutos"]} min"
        )
    return "\n".join(linhas)

def executar():
    inicio = time.time()
    logger.info("Iniciando execucao do robo de manutencao.")

    try:
        df_bruto = carregar_dados()
        logger.info(f"CSV carregando com {len(df_bruto)} linhas.")

        df_limpo, removidas = limpar_dados(df_bruto)
        if removidas > 0:
            logger.warning(f"{removidas} linha(s) descartada(s) na limpeza.")

        df_processando, resumo = calcular_kpis(df_limpo)
        logger.info(f"KPIs calculados para {len(resumo)} equipamento(s).")

        caminho_relatorio = gerar_relatorio_excel(resumo)
        logger.info(f"Relatorio gerado em: {caminho_relatorio}")

        resumo_texto = montar_resumo_texto(resumo)
        enviar_relatorio_por_email(caminho_relatorio, resumo_texto)
        logger.info("E-mail enviado com sucesso.")

    except FileNotFoundError as erro:
        logger.error(f"Arquivo de entrada não encontrado: {erro}")
        raise
    except Exception as erro:
        logger.error(f"Falha inesperada na execucao do robo: {erro}")
        raise
    finally:
        duracao = round(time.time() - inicio, 2)
        logger.info(f"Execucao finalida em{duracao} segundos.")

if __name__ == "__main__":
    executar()
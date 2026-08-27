import pandas as pd
from src.config import CAMINHO_CSV_ENTRADA, LIMITE_PARADAS_CRITICO

def carregar_dados():
    df = pd.read_csv(
        CAMINHO_CSV_ENTRADA,
        parse_dates=["data_hora_inicio", "data_hora_fim"]
    )
    return df

def limpar_dados(df):
    antes = len(df)

    df = df.drop_duplicates()

    df = df.dropna(subset=["data_hora_inicio", "data_hora_fim", "equipamento"])

    df = df[df["data_hora_fim"] > df["data_hora_inicio"]]

    depois = len(df)

    linhas_removidas = antes - depois

    return df, linhas_removidas

def calcular_kpis(df):
    df["duracao_minutos"] = (
        (df["data_hora_fim"] - df["data_hora_inicio"]).dt.total_seconds() / 60
    )

    resumo = df.groupby("equipamento").agg(
        total_paradas=("equipamento", "count"),
        duracao_media_minutos=("duracao_minutos", "mean"),
        duracao_total_minutos=("duracao_minutos")
    )

def calcular_kpis(df):
    df["duracao_minutos"] = (
        (df["data_hora_fim"] - df["data_hora_inicio"]).dt.total_seconds() / 60
    )

    resumo = df.groupby("equipamento").agg(
        total_paradas=("equipamento", "count"),
        duracao_media_minutos=("duracao_minutos", "mean"),
        duracao_total_minutos=("duracao_minutos", "sum"),
    ).reset_index()

    resumo["duracao_media_minutos"] = resumo["duracao_media_minutos"].round(1)
    resumo["duracao_total_minutos"] = resumo["duracao_total_minutos"].round(1)

    resumo["critico"] = resumo["total_paradas"] >= LIMITE_PARADAS_CRITICO

    resumo = resumo.sort_values("total_paradas", ascending=False)

    return df, resumo
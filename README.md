# RPA Manutencao Industrial

Robo em Python que automatiza a geracao e o envio de relatorios diarios de
manutencao industrial, eliminando um processo antes feito manualmente em
planilhas.

## O que ele faz
- Le dados brutos de paradas de equipamento (CSV exportado de sistema SCADA)
- Limpa e valida os dados (duplicatas, campos vazios, duracoes invalidas)
- Calcula KPIs por equipamento: total de paradas, duracao media e total
- Gera um relatorio Excel formatado, com destaque automatico para
  equipamentos criticos
- Envia o relatorio por e-mail automaticamente
- Registra cada execucao em log, com tratamento de erros

## Stack
Python 3.13, pandas, openpyxl, python-dotenv, smtplib, logging

## Como rodar
1. python -m venv venv
2. .\venv\Scripts\Activate.ps1
3. pip install -r requirements.txt
4. Copie .env.example para .env e preencha suas credenciais
5. python -m src.main
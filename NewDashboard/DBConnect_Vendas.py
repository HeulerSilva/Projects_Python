import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def carregar_dados():
    server = os.getenv('DB_SERVER')
    username = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    driver = os.getenv('DB_DRIVER')

    connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
    engine_conexao = create_engine(connection_string)
    return engine_conexao

engine = carregar_dados()

query = """SELECT * FROM vw_Vendas_Produtivas ORDER BY 1,2,3"""
df_agrupado = pd.read_sql(query, engine)

linhas = df_agrupado.shape[0]
print(f'O arquivo otimizado possui apenas {linhas} linhas agrupadas.')

grafico = px.histogram(
    df_agrupado, 
    x='MES', 
    y='TOTAL_VENDA',
    color='ANO',
    title='Total Vendas por Mês e Ano',
    labels={'TOTAL_VENDA': 'Total Vendas (R$)', 'ANO': 'Ano', 'MES': 'Mês'}
)

grafico.update_xaxes(categoryorder='category ascending')
grafico.update_traces(texttemplate='%{y:,.2f}')

arquivo = "GraficoVendas.html"
grafico.write_html(arquivo)
import webbrowser
import os
webbrowser.open('file://' + os.path.realpath(arquivo))
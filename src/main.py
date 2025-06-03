import pandas as pd
import sqlite3

def carregar_csv(path, sep=','):
    return pd.read_csv(path, sep=sep)

def carregar_excel(path, sheet_name):
    return pd.read_excel(path, sheet_name=sheet_name)

def carregar_html(path):
    tabelas = pd.read_html(path)
    return tabelas[0] if tabelas else None

def carregar_h5(path):
    return pd.read_hdf(path)

def carregar_json(path):
    return pd.read_json(path)

def carregar_xml(path):
    return pd.read_xml(path)

def carregar_sqlite(path, query):
    conexao = sqlite3.connect(path)
    return pd.read_sql_query(query, conexao)

def exibir_df(df, linhas=5):
    print(df.head(linhas))


if __name__ == "__main__":
    print("Início da aquisição de dados.\n")

    df_csv = carregar_csv('data/base_vendas.csv')
    exibir_df(df_csv)

    df_csv_pv = carregar_csv('data/base_vendas_ponto_virgula.csv', sep=';')
    exibir_df(df_csv_pv)

    df_tsv = carregar_csv('data/base_vendas_tab.tsv', sep='\t')
    exibir_df(df_tsv)

    df_func = carregar_excel('data/Vendas.xlsx', 'funcionarios')
    df_vendas = carregar_excel('data/Vendas.xlsx', 'base_vendas')
    exibir_df(df_func)
    exibir_df(df_vendas)

    df_html = carregar_html('data/base_vendas.html')
    exibir_df(df_html)

    df_h5 = carregar_h5('data/base_vendas.h5')
    exibir_df(df_h5)

    df_json = carregar_json('data/base_vendas.json')
    exibir_df(df_json)

    df_xml = carregar_xml('data/base_vendas.xml')
    exibir_df(df_xml)

    df_sql = carregar_sqlite('data/vendas.db', 'SELECT * FROM pedidos')
    exibir_df(df_sql)
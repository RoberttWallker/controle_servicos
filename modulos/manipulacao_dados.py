from .metodos import cadastro_servico
import pandas as pd
from pathlib import Path

#Configurar o caminho onde o arquivo será salvo
current_path = Path(__file__).parent
ROOT_PATH = current_path.parent
input_path = ROOT_PATH / "data" / "input"
arquivo_excel = input_path / "controle de servicos.xlsx"

df = pd.DataFrame(columns=[
    'OS',
    'LOJA',
    'DATA ENTRADA',
    'DATA SAÍDA',
    'DESCRIÇÃO PEÇA',
    'DESCRIÇÃO SERVIÇO',
    'PESO ENTRADA',
    'PESO SAÍDA'
    ])

def verifica_cria(df):
    novo_servico = cadastro_servico()
    if arquivo_excel.exists():
        df_existente = pd.read_excel(arquivo_excel, engine='openpyxl')
        df = pd.concat([df_existente, pd.DataFrame([novo_servico])], ignore_index=True)
    else:
        df = pd.concat([df, pd.DataFrame([novo_servico])], ignore_index=True)
    df.to_excel(arquivo_excel, index=False, engine='openpyxl')
    return df

def verifica_cria_tk(df, novo_servico):
    if arquivo_excel.exists():
        df_existente = pd.read_excel(arquivo_excel, engine='openpyxl')
        df = pd.concat([df_existente, pd.DataFrame([novo_servico])], ignore_index=True)
    else:
        df = pd.concat([df, pd.DataFrame([novo_servico])], ignore_index=True)
    df.to_excel(arquivo_excel, index=False, engine='openpyxl')
    return df


from .classes import Servicos
from .manipulacao_dados import verifica_cria_tk, df
from datetime import datetime
import tkinter as tk
from tkinter import ttk

df1 = df

def cadastro_servico_tk():
    os = int(entry_os.get())
    loja = str(entry_loja.get())
    data_entrada = datetime.strptime(entry_data_entrada.get(), "%d/%m/%Y")
    data_saida = datetime.strptime(entry_data_saida.get(), "%d/%m/%Y")
    descricao_peca = str(entry_descricao_peca.get())
    descricao_servico = str(entry_descricao_servico.get())
    peso_entrada = float(entry_peso_entrada.get())
    peso_saida = float(entry_peso_saida.get())
    # Criando objeto Servicos
    servico = Servicos(
        os,
        loja,
        data_entrada,
        data_saida,
        descricao_peca,
        descricao_servico,
        peso_entrada,
        peso_saida
    )
    # Criando o dicionário com os valores
    novo_servico = {
        'OS': servico.numero_os,
        'LOJA': servico.loja,
        'DATA ENTRADA': servico.data_entrada,
        'DATA SAÍDA': servico.data_saida,
        'DESCRIÇÃO PEÇA': servico.descricao_peca,
        'DESCRIÇÃO SERVIÇO': servico.descricao_servico,
        'PESO ENTRADA': servico.peso_entrada,
        'PESO SAÍDA': servico.peso_saida
    }
    return novo_servico
    
def verifica_cria_df():
    novo_servico = cadastro_servico_tk()
    verifica_cria_tk(df1, novo_servico)


#Criando a app principal

app = tk.Tk()
app.title("Cadastro de Serviço")

#Aplicando tema ttk
style = ttk.Style(app)
style.theme_use("clam")

#Labels e campos de entrada com 'ttk.Entry'
ttk.Label(app, text='Número OS:').grid(row=0, column=0, padx=10, pady=5)
entry_os = ttk.Entry(app)
entry_os.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(app, text='Loja').grid(row=1, column=0, padx=10, pady=5)
entry_loja = ttk.Entry(app)
entry_loja.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(app, text='Data de entrada - DD/MM/AAAA:').grid(row=2, column=0, padx=10, pady=5)
entry_data_entrada = ttk.Entry(app)
entry_data_entrada.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(app, text='Data de Saída (DD/MM/AAAA):').grid(row=3, column=0, padx=10, pady=5)
entry_data_saida = ttk.Entry(app)
entry_data_saida.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(app, text='Descrição peça:').grid(row=4, column=0, padx=10, pady=5)
entry_descricao_peca = ttk.Entry(app)
entry_descricao_peca.grid(row=4, column=1, padx=10, pady=5)

ttk.Label(app, text='Descrição serviço').grid(row=5, column=0, padx=10, pady=5)
entry_descricao_servico = ttk.Entry(app)
entry_descricao_servico.grid(row=5, column=1, padx=10, pady=5)

ttk.Label(app, text='Peso entrada').grid(row=6, column=0, padx=10, pady=5)
entry_peso_entrada = ttk.Entry(app)
entry_peso_entrada.grid(row=6, column=1, padx=10, pady=5)

ttk.Label(app, text='Peso saida').grid(row=7, column=0, padx=10, pady=5)
entry_peso_saida = ttk.Entry(app)
entry_peso_saida.grid(row=7, column=1, padx=10, pady=5)



#Botão de salvar com 'ttk.Button'
ttk.Button(app, text='Salvar', command=verifica_cria_df).grid(row=8, column=1, pady=10)


#Iniciando o loop da interface
app.mainloop()
from .classes import Servicos
from .manipulacao_dados import verifica_cria_tk, df
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

df1 = df


def tela_inicial():
    #Criando a app principal

    app = tk.Tk()
    app.title("SGS")


    #Aplicando tema ttk
    style = ttk.Style(app)
    style.theme_use("clam")
    app.geometry("600x600")




    def criar_janela_cadastro():
        def cadastro_servico_tk():
            try:    
                os = int(entry_os.get())
                loja = str(entry_loja.get())
                data_entrada = datetime.strptime(entry_data_entrada.get(), "%d/%m/%Y")
                data_saida = datetime.strptime(entry_data_saida.get(), "%d/%m/%Y")
                descricao_peca = str(text_descricao_peca.get("1.0", "end"))
                descricao_servico = str(text_descricao_servico.get("1.0", "end"))
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
                messagebox.showinfo("Sucesso!","Serviço cadastrado com sucesso!")
                return novo_servico
            except NameError as e:
                messagebox.showerror("Erro!",f"Ocorreu um erro do tipo: {e}")
                
        def verifica_cria_df():
            novo_servico = cadastro_servico_tk()
            try:
                verifica_cria_tk(df1, novo_servico)
            except NameError as e:
                messagebox.showerror("Erro", f"Ocorreu um erro do tipo: {e}")

        janela_cadastro = tk.Toplevel(app)
        janela_cadastro.geometry("600x600")
        janela_cadastro.title("Cadastro de Serviço")
        

        #Labels e campos de entrada com 'ttk.Entry'
        ttk.Label(janela_cadastro, text='Número OS:').grid(row=0, column=0, padx=10, pady=5)
        entry_os = ttk.Entry(janela_cadastro)
        entry_os.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(janela_cadastro, text='Loja').grid(row=1, column=0, padx=10, pady=5)
        entry_loja = ttk.Entry(janela_cadastro)
        entry_loja.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(janela_cadastro, text='Data de entrada - DD/MM/AAAA:').grid(row=2, column=0, padx=10, pady=5)
        entry_data_entrada = ttk.Entry(janela_cadastro)
        entry_data_entrada.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(janela_cadastro, text='Data de Saída (DD/MM/AAAA):').grid(row=3, column=0, padx=10, pady=5)
        entry_data_saida = ttk.Entry(janela_cadastro)
        entry_data_saida.grid(row=3, column=1, padx=10, pady=5)

        scrollbar_peca = ttk.Scrollbar(janela_cadastro, orient="vertical")
        scrollbar_peca.grid(row=4, column=2, sticky='ns')
        ttk.Label(janela_cadastro, text='Descrição peça:').grid(row=4, column=0, padx=10, pady=5)
        text_descricao_peca = tk.Text(janela_cadastro, width= 40, height=10)
        text_descricao_peca.grid(row=4, column=1, padx=10, pady=5)
        scrollbar_peca.config(command=text_descricao_peca.yview)

        ttk.Label(janela_cadastro, text='Descrição serviço').grid(row=5, column=0, padx=10, pady=5)
        text_descricao_servico = tk.Text(janela_cadastro, width=40, height=10)
        text_descricao_servico.grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(janela_cadastro, text='Peso entrada').grid(row=6, column=0, padx=10, pady=5)
        entry_peso_entrada = ttk.Entry(janela_cadastro)
        entry_peso_entrada.grid(row=6, column=1, padx=10, pady=5)

        ttk.Label(janela_cadastro, text='Peso saida').grid(row=7, column=0, padx=10, pady=5)
        entry_peso_saida = ttk.Entry(janela_cadastro)
        entry_peso_saida.grid(row=7, column=1, padx=10, pady=5)



        #Botão de salvar com 'ttk.Button'
        ttk.Button(janela_cadastro, text='Salvar', command=verifica_cria_df).grid(row=8, column=1, pady=10)

    #Criando tela de inicial
    botao_cadastro = ttk.Button(app, width=30, padding=30, text='Cadastrar Serviço', command=criar_janela_cadastro)
    botao_cadastro.grid(row=0, column=0, padx=10, pady=5)

    botao_fechar = ttk.Button(app, width=30, padding=30, text='Cancelar', command="")
    botao_fechar.grid(row=1, column=0, padx=10, pady=5)

    #Iniciando o loop da interface
    app.mainloop()
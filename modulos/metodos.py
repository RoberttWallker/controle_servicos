from datetime import datetime
from .classes import Servicos

def cadastro_servico():
    os = int(input("Numero os: "))
    loja = input("Loja: ")
    data_entrada = datetime.strptime(input("Data de entrada - DD/MM/AAAA: "),"%d/%m/%Y")
    data_saida = datetime.strptime(input("Data saída - DD/MM/AAAA: "),"%d/%m/%Y")
    descrica_peca = input("Descrição peça: ")
    descricao_servico = input("Descrição serviço: ")
    peso_entrada = float(input("Peso de entrada: "))
    peso_saida = float(input("Peso saída: "))
    servico = Servicos(
        os,
        loja,
        data_entrada,
        data_saida,
        descrica_peca,
        descricao_servico,
        peso_entrada,
        peso_saida
    )
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
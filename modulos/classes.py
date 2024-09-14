class Servicos:
    def __init__(
            self,
            numero_os,
            loja,
            data_entrada,
            data_saida,
            descricao_peca,
            descricao_servico,
            peso_entrada,
            peso_saida):
        self.numero_os = numero_os
        self.loja = loja
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.descricao_peca = descricao_peca
        self.descricao_servico = descricao_servico
        self.peso_entrada = peso_entrada
        self.peso_saida = peso_saida

    def to_dict(self):
        return vars(self)
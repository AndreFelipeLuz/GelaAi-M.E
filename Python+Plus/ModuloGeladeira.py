class GeladeiraInteligente:
    def __init__(self):
        self.itens = {}
        self.alerta_prox_validade = []
        self.historico_remocao = []

    def adicionar_item(self, nome, quantidade, prox_validade=None):
        if nome in self.itens:
            self.itens[nome] += quantidade
        else:
            self.itens[nome] = quantidade

        if prox_validade is not None:
            if prox_validade <= 7:
                self.alerta_prox_validade.append(nome)

    def remover_item(self, nome, quantidade):
        if nome in self.itens and self.itens[nome] >= quantidade:
            self.itens[nome] -= quantidade
            self.historico_remocao.append((nome, quantidade))
            return True
        else:
            return False

    def verificar_disponibilidade(self, nome):
        return self.itens.get(nome, 0)

    def listar_itens(self):
        return self.itens

    def listar_alertas_prox_validade(self):
        return self.alerta_prox_validade

    def listar_historico_remocao(self):
        return self.historico_remocao


geladeira = GeladeiraInteligente()
geladeira.adicionar_item("Coca-Cola", 2, 5)
geladeira.adicionar_item("Água", 12, 10)
geladeira.adicionar_item("Guaraná", 6, 3)

print("Itens na geladeira:", geladeira.listar_itens())
print("Alertas de itens próximos à validade:", geladeira.listar_alertas_prox_validade())

geladeira.remover_item("Coca-Cola", 1)
geladeira.remover_item("Água", 6)

print("Itens na geladeira após remoção:", geladeira.listar_itens())
print("Histórico de remoção:", geladeira.listar_historico_remocao())
import pytest
from ModuloGeladeira import GeladeiraInteligente

def test_adicionar_item():
    geladeira = GeladeiraInteligente()
    geladeira.adicionar_item("Coca-Cola", 2, 5)
    assert geladeira.itens["Coca-Cola"] == 2


def test_remover_item():
    geladeira = GeladeiraInteligente()
    geladeira.adicionar_item("Coca-Cola", 2, 5)
    geladeira.remover_item("Coca-Cola", 1)
    assert geladeira.itens["Coca-Cola"] == 1


def test_verificar_disponibilidade():
    geladeira = GeladeiraInteligente()
    geladeira.adicionar_item("Coca-Cola", 2, 5)
    assert geladeira.verificar_disponibilidade("Coca-Cola") == 2


def test_listar_itens():
    geladeira = GeladeiraInteligente()
    geladeira.adicionar_item("Coca-Cola", 2, 5)
    geladeira.adicionar_item("Água", 12, 10)
    geladeira.adicionar_item("Guaraná", 6, 3)
    assert geladeira.listar_itens() == {"Coca-Cola": 2, "Água": 12, "Guaraná": 6}


def test_listar_alertas_prox_validade():
    geladeira = GeladeiraInteligente()
    geladeira.adicionar_item("Coca-Cola", 2, 5)
    geladeira.adicionar_item("Água", 12, 10)
    geladeira.adicionar_item("Guaraná", 6, 3)
    assert geladeira.listar_alertas_prox_validade() == ['Coca-Cola', 'Guaraná']


def test_listar_historico_remocao():
    geladeira = GeladeiraInteligente()
    geladeira.adicionar_item("Coca-Cola", 2, 5)
    geladeira.adicionar_item("Água", 12, 10)
    geladeira.adicionar_item("Guaraná", 6, 3)
    geladeira.remover_item("Coca-Cola", 1)
    geladeira.remover_item("Água", 6)
    assert geladeira.listar_historico_remocao() == ([("Coca-Cola", 1), ("Água", 6)])
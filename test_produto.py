import pytest
from produto import Produto

def teste_novo_produto():
    produto = Produto('Camiseta Mickey', 50.0)
    assert produto.nome == 'Camiseta Mickey'
    assert produto.preco == 50.0
    assert produto.estoque == 0

def teste_adicionar_estoque():
    produto = Produto('Camiseta Mickey', 50.0)
    produto.adicionar_estoque(10)
    assert produto.estoque == 10

def teste_vender_produto():
    produto = Produto('Camiseta Mickey', 50.0)
    produto.adicionar_estoque(10)
    produto.vender_produto(5)
    assert produto.estoque == 5

def teste_vender_produto_sem_estoque():
    produto = Produto('Camiseta Mickey', 50.0)
    produto.adicionar_estoque(10)
    with pytest.raises(ValueError):
        produto.vender_produto(15)
    
def teste_vender_produto_estoque_negativo():
    produto = Produto('Camiseta Mickey', 50.0)
    with pytest.raises(ValueError):
        produto.vender_produto(15)

pytest.main()
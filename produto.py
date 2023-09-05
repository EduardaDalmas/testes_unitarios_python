class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.estoque = 0

    def adicionar_estoque(self, quantidade):
        if quantidade < 0:
            raise ValueError('Não é possível adicionar estoque negativo')
        self.estoque += quantidade

    def vender_produto(self, quantidade):
        if quantidade < 0:
            raise ValueError('Não é possível vender um produto com estoque negativo')
        if quantidade > self.estoque:
            raise ValueError('Não é possível vender um produto com estoque insuficiente')
        self.estoque -= quantidade

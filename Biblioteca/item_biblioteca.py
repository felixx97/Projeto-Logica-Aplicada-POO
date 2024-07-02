class ItemBiblioteca:
    def __init__(self, id, titulo, descricao, quantidade, ano_lancamento):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.quantidade = quantidade
        self.ano_lancamento = ano_lancamento
        self.disponivel = quantidade > 0

    def emprestar(self):
        if self.disponivel:
            self.quantidade -= 1
            if self.quantidade == 0:
                self.disponivel = False
            return True
        return False

    def devolver(self):
        self.quantidade += 1
        self.disponivel = True


class Livro(ItemBiblioteca):
    def __init__(self, id, titulo, descricao, quantidade, ano_lancamento, autor):
        super().__init__(id, titulo, descricao, quantidade, ano_lancamento)
        self.autor = autor


class Revista(ItemBiblioteca):
    def __init__(self, id, titulo, descricao, quantidade, ano_lancamento, edicao):
        super().__init__(id, titulo, descricao, quantidade, ano_lancamento)
        self.edicao = edicao


class DVD(ItemBiblioteca):
    def __init__(self, id, titulo, descricao, quantidade, ano_lancamento, duracao):
        super().__init__(id, titulo, descricao, quantidade, ano_lancamento)
        self.duracao = duracao


class CD(ItemBiblioteca):
    def __init__(self, id, titulo, descricao, quantidade, ano_lancamento, duracao):
        super().__init__(id, titulo, descricao, quantidade, ano_lancamento)
        self.duracao = duracao

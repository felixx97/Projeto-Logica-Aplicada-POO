from datetime import datetime


class Emprestimo:
    def __init__(self, item, usuario):
        self.item = item
        self.usuario = usuario
        self.data_emprestimo = datetime.now()

    def realizar_emprestimo(self):
        return self.usuario.emprestar_item(self.item)

    def realizar_devolucao(self):
        return self.usuario.devolver_item(self.item)

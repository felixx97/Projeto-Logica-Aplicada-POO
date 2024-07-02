from datetime import datetime


class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.emprestimos = []
        self.historico = []

    def emprestar_item(self, item):
        if item.emprestar():
            self.emprestimos.append((item, datetime.now()))
            self.historico.append((item, datetime.now()))
            return True
        return False

    def devolver_item(self, item):
        for emprestimo in self.emprestimos:
            if emprestimo[0] == item:
                item.devolver()
                self.emprestimos.remove(emprestimo)
                return True
        return False


class Aluno(Usuario):
    def __init__(self, id, nome, curso):
        super().__init__(id, nome)
        self.curso = curso


class Professor(Usuario):
    def __init__(self, id, nome, departamento):
        super().__init__(id, nome)
        self.departamento = departamento


class Funcionario(Usuario):
    def __init__(self, id, nome, setor):
        super().__init__(id, nome)
        self.setor = setor

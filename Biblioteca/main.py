from item_biblioteca import Livro, Revista, DVD, CD
from usuario import Aluno, Professor, Funcionario, Usuario
from emprestimo import Emprestimo
from datetime import datetime

itens = {}
usuarios = {}
id_counter = 1


def cadastrar_item():
    global id_counter
    print("\nEscolha o tipo do item:")
    print("1. Livro")
    print("2. Revista")
    print("3. DVD")
    print("4. CD")
    tipo = input("Escolha uma opção (1-4): ").strip()

    titulo = input("Título do item: ").strip()
    descricao = input("Descrição do item: ").strip()
    quantidade = int(input("Quantidade do item: ").strip())
    ano_lancamento = input("Ano de lançamento: ").strip()

    for item in itens.values():
        if item.titulo == titulo and item.descricao == descricao:
            print("Item já cadastrado.")
            return

    if tipo == '1':
        autor = input("Autor: ").strip()
        item = Livro(id_counter, titulo, descricao,
                     quantidade, ano_lancamento, autor)
    elif tipo == '2':
        edicao = input("Edição: ").strip()
        item = Revista(id_counter, titulo, descricao,
                       quantidade, ano_lancamento, edicao)
    elif tipo == '3':
        duracao = input("Duração (em minutos): ").strip()
        item = DVD(id_counter, titulo, descricao,
                   quantidade, ano_lancamento, duracao)
    elif tipo == '4':
        duracao = input("Duração (em minutos): ").strip()
        item = CD(id_counter, titulo, descricao,
                  quantidade, ano_lancamento, duracao)
    else:
        print("Tipo de item inválido.")
        return

    itens[id_counter] = item
    id_counter += 1
    print(f"Item {titulo} cadastrado com sucesso.")


def cadastrar_usuario():
    print("\nEscolha o tipo do usuário:")
    print("1. Aluno")
    print("2. Professor")
    print("3. Funcionário")
    tipo = input("Escolha uma opção (1-3): ").strip()

    username = input("Username: ").strip()
    nome = input("Nome do usuário: ").strip()

    if username in usuarios:
        print("Usuário já cadastrado.")
        return

    if tipo == '1':
        curso = input("Curso: ").strip()
        usuario = Aluno(username, nome, curso)
    elif tipo == '2':
        departamento = input("Departamento: ").strip()
        usuario = Professor(username, nome, departamento)
    elif tipo == '3':
        setor = input("Setor: ").strip()
        usuario = Funcionario(username, nome, setor)
    else:
        print("Tipo de usuário inválido.")
        return

    usuarios[username] = usuario
    print(f"Usuário {nome} cadastrado com sucesso.")


def emprestar_item():
    username = input("Username do usuário: ").strip()
    id_item = int(input("ID do item: ").strip())

    if username in usuarios and id_item in itens:
        usuario = usuarios[username]
        item = itens[id_item]
        emprestimo = Emprestimo(item, usuario)
        if emprestimo.realizar_emprestimo():
            print(
                f"Item {item.titulo} emprestado com sucesso para {usuario.nome}.")
        else:
            print(f"Item {item.titulo} não está disponível.")
    else:
        print("Usuário ou item não encontrado.")


def devolver_item():
    username = input("Username do usuário: ").strip()
    id_item = int(input("ID do item: ").strip())

    if username in usuarios and id_item in itens:
        usuario = usuarios[username]
        item = itens[id_item]
        if usuario.devolver_item(item):
            print(
                f"Item {item.titulo} devolvido com sucesso por {usuario.nome}.")
        else:
            print(f"Item {item.titulo} não foi emprestado por {usuario.nome}.")
    else:
        print("Usuário ou item não encontrado.")


def relatorio_itens_disponiveis():
    print("\nItens disponíveis:")
    for item in itens.values():
        if item.disponivel:
            print(
                f"ID: {item.id}, Título: {item.titulo}, Quantidade: {item.quantidade}")


def relatorio_emprestimos_usuario():
    username = input("Username do usuário: ").strip()
    if username in usuarios:
        usuario = usuarios[username]
        print(f"\nEmpréstimos atuais de {usuario.nome}:")
        for emprestimo in usuario.emprestimos:
            item, data = emprestimo
            print(f"ID: {item.id}, Título: {item.titulo}, Data: {data}")
        print(f"\nHistórico de empréstimos de {usuario.nome}:")
        for emprestimo in usuario.historico:
            item, data = emprestimo
            print(f"ID: {item.id}, Título: {item.titulo}, Data: {data}")
    else:
        print("Usuário não encontrado.")


def main():
    while True:
        print("\n--- Biblioteca ---")
        print("1. Cadastrar item")
        print("2. Cadastrar usuário")
        print("3. Emprestar item")
        print("4. Devolver item")
        print("5. Relatório de itens disponíveis")
        print("6. Relatório de empréstimos do usuário")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_item()
        elif opcao == '2':
            cadastrar_usuario()
        elif opcao == '3':
            emprestar_item()
        elif opcao == '4':
            devolver_item()
        elif opcao == '5':
            relatorio_itens_disponiveis()
        elif opcao == '6':
            relatorio_emprestimos_usuario()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

from biblioteca import Biblioteca
from livros import Livros
def ExibirMenu():
    print("1. Adicionar Livro\n2. Consultar detalhes do livro\n3. Emprestar Livro\n4. Listar livros da biblioteca\n5. Devolver livro\n6. Sair ")
biblioteca = Biblioteca()
while True:
    ExibirMenu()
    op = int(input("Digite a opção: "))
    if op == 1:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        livro_ = Livros(titulo, autor)
        biblioteca.AdicionarLivro(livro_)
    elif op == 2:
        titulo = input("Digite o livro que deseja procurar: ")
        detalhes = biblioteca.ConsultarDetalhes(titulo)
        print(detalhes)
    elif op == 3:
        titulo = input("Digite o título que quer buscar: ")
        biblioteca.EmprestarLivro(titulo)
    elif op == 4:
        biblioteca.ListarLivro()
    elif op == 5:
        titulo = input("Digite o título que quer buscar: ")
        biblioteca.DevolverLivro(titulo)
    elif op == 6:
        break
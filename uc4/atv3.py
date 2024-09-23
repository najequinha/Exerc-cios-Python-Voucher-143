class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
    def altEd(self):
        self.editora = input("Alterar a editora: ")
        print(f"Editora: {self.editora}")
    def pag(self):
        print(f"Número de páginas: {self.paginas}")
livro1 = Livro("Livro", "Autor", "Editora", 0)
livro1.altEd()
livro1.pag()
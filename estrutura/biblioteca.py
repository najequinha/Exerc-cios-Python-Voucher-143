class Biblioteca:
    def __init__(self):
        self.livros = []

    def AdicionarLivro(self, livro):
            print(livro)
            # self.livros.append(livro)
            # for i in self.livros: 
            #     print(i)
    def BuscarLivro(self, titulo):
        for lupa in self.livros:
            if lupa.titulo == titulo:
                return lupa
    def ConsultarDetalhes(self, titulo):
        livro = self.BuscarLivro(titulo)
        if livro:
            return livro
        else:
            print("Livro não encontrado.")
    def EmprestarLivro(self, titulo):
        livro = self.BuscarLivro(titulo)
        if livro:
            if livro.emprestado == False:
                print("Empréstimo realizado.")
                livro.emprestado = True
            else:
                print("Livro já emprestado.")
        else:
            print("Livro não encontrado.")
    def DevolverLivro(self, titulo):
            livro = self.BuscarLivro(titulo)
            if livro:
                if livro.emprestado == True:
                    print("Devolvido com sucesso")
                    livro.emprestado = False
                else:
                    print("O livro não está emprestado para devolver.")
            else:
                print("Livro não encontrado.")
    def ListarLivro(self):
        for i in self.livros:
            print(i)
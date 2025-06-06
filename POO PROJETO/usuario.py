from datetime import date

class Usuario:
    def __init__(self, nome: str, id: int):
        self._nome = nome
        self._id = id
        self._livros_emprestados = []
    
    @property
    def nome(self):
        return self._nome
    
    def emprestar_livro(self, livro):
        if livro.emprestar():
            self._livros_emprestados.append(livro)
            return True
        return False
    
    def devolver_livro(self, livro):
        if livro in self._livros_emprestados:
            livro.devolver()
            self._livros_emprestados.remove(livro)
            return True
        return False
    
    def __str__(self):
        return f"Usuário: {self._nome} (ID: {self._id})"

class Professor(Usuario):
    def __init__(self, nome: str, id: int, departamento: str):
        super().__init__(nome, id)
        self._departamento = departamento
        self._limite_emprestimos = 10
    
    def __str__(self):
        return f"Professor {self._nome} do departamento de {self._departamento}"
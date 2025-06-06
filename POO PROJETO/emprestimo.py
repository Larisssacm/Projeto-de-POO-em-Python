from datetime import date


class Emprestimo:
    def __init__(self, livro, usuario, data_emprestimo):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None
    
    def registrar_devolucao(self):
        self.data_devolucao = date.today()
        self.usuario.devolver_livro(self.livro)
    
    def __str__(self):
        status = "Em empréstimo" if not self.data_devolucao else f"Devolvido em {self.data_devolucao}"
        return f"Empréstimo de {self.livro.titulo} para {self.usuario.nome} - {status}"
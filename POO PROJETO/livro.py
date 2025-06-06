class Livro:
    def __init__(self, titulo: str, autor: str, isbn: str):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponivel = True

    @property
    def titulo(self):
        return self._titulo
    
    @property
    def disponivel(self):
        return self._disponivel
    
    def emprestar(self):
        if self._disponivel:
            self._disponivel = False
            return True
        return False
    
    def devolver(self):
        self._disponivel = True
    
    def __str__(self):
        return f"{self._titulo} por {self._autor} ({'Disponível' if self._disponivel else 'Emprestado'})"
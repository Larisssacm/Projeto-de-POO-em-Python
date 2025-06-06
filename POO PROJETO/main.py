from livro import Livro
from usuario import Usuario, Professor
from emprestimo import Emprestimo
from datetime import date, timedelta

def main():
    # Criando objetos
    livro1 = Livro("Python Fluente", "Luciano Ramalho", "978-85-7522-331-8")
    livro2 = Livro("Clean Code", "Robert C. Martin", "978-85-7452-257-3")
    
    prof = Professor("Carlos Silva", 123, "Ciência da Computação")
    aluno = Usuario("Maria Oliveira", 456)
    
    # Demonstração de funcionalidades
    print("\n=== Sistema de Biblioteca ===")
    print(livro1)
    print(livro2)
    print(prof)
    print(aluno)
    
    # Empréstimos
    prof.emprestar_livro(livro1)
    aluno.emprestar_livro(livro2)
    
    print("\nApós empréstimos:")
    print(livro1)
    print(livro2)
    
    # Criando e registrando empréstimo
    emprestimo = Emprestimo(livro1, prof, date.today())
    print("\nRegistro de empréstimo:")
    print(emprestimo)
    
    # Devolução
    emprestimo.registrar_devolucao()
    print("\nApós devolução:")
    print(emprestimo)
    print(livro1)

if __name__ == "__main__":
    main()
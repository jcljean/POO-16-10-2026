from dvd import DVD
from editora import Editora
from emprestimo import Emprestimo
from livro import Livro
from mapa import Mapa
from revista import Revista

editora1 = Editora("Editora Exemplo", "São Paulo")

livro1 = Livro("Python para Todos", 2021)
dvd1 = DVD("Matrix", 1999)
piaui = Revista("Piaui", 2023)
##brasil = Mapa("Mapa do Brasil", 2020, "1:5.000.000")

acervo = [livro1, dvd1, piaui]

for item in acervo:
    print(item.titulo, item.prazoEmpr())

##try:
 ## emp3 = Emprestimo("Ana", piaui, "09/10/2026")
 ## print(emp3.resumo())
##except ValueError as erro:
 ## print("barrou:", erro)
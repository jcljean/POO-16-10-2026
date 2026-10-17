from abc import ABC, abstractmethod

class ItemAcervo(ABC):
    def __init__(self, titulo,ano):
        self.titulo = titulo
        self.ano = ano
    
    @abstractmethod
    def prazoEmpr(self):
        pass

class Livro(ItemAcervo):
    def __init__(self, titulo, ano):
       super().__init__(titulo, ano)
    
    def prazoEmpr(self):
        return "14 dias"

class DVD(ItemAcervo):
    def __init__(self, titulo, ano):
        super().__init__(titulo, ano)
    
    def prazoEmpr(self):
        return '2 dias'

class Revista(ItemAcervo):
    def __init__(self, titulo, ano):
        super().__init__(titulo, ano)
    
    def prazoEmpr(self):
        return "3 dias"

ItensAcervo = [
    Livro("O Senhor dos Anéis", 1954),
    DVD("Matrix", 1999),
    Revista("National Geographic", 2021)]

for item in ItensAcervo:
    print(item.titulo, item.prazoEmpr())

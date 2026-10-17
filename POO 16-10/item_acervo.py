from abc import ABC, abstractmethod

class ItemAcervo(ABC):
    def __init__(self, titulo,ano):
        self.titulo = titulo
        self.ano = ano
    
    @abstractmethod
    def prazoEmpr(self):
        pass
from item_acervo import ItemAcervo

class DVD(ItemAcervo):
    def __init__(self, titulo, ano):
        super().__init__(titulo, ano)
    
    def prazoEmpr(self):
        return '2 dias'
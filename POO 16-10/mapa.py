from item_acervo import ItemAcervo


class Mapa(ItemAcervo):

  def __init__(self, titulo, ano, escala):
    super().__init__(titulo, ano)
    self.escala = escala

  def prazo_de_emprestimo(self):
    return 7
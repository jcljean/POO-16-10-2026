class Emprestimo:

  def __init__(self, aluno, livro, data):

    if livro.prazo_de_emprestimo() == 0:
      raise ValueError(f"{livro.titulo} não pode ser emprestado")

    self.aluno = aluno
    self.livro = livro
    self.data = data
    self.devolvido = False

  def resumo(self):
    return f"Empréstimo: {self.livro.titulo} para {self.aluno.nome} em {self.data}"
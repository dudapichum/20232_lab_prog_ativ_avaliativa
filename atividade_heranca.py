## Exercício 2 - Herança
class Produto:
  def __init__(self, nome):
    self.nome = nome
 
  def imprimir_informacoes(self):
    print("Nome:", self.nome)

 
 
class Fruta(Produto):
  def __init__(self, nome, cor):
    super().__init__(nome)
    self.cor = cor
 
  def imprimir_informacoes(self):
    super().imprimir_informacoes()
    print("Cor:", self.cor)
 
 
fruta = Fruta("Maçã", "Vermelha")
fruta.imprimir_informacoes()

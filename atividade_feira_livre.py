## Exercício 1 - Sistema de Livre

class FeiraLivre:
  def __init__(self, frutas, legumes):
    self.frutas = frutas
    self.legumes = legumes
 
  def imprimir_lista(self):
    print("Lista de frutas:")
    for fruta in self.frutas:
      print(fruta)
    print()
    print("Lista de legumes:")
    for legume in self.legumes:
      print(legume)
 
 
  def solicitar_fruta_ou_legume(self):
    fruta_ou_legume = input("Deseja selecionar uma fruta (F) ou um legume (L)? ")
    return fruta_ou_legume
 
  def imprimir_informacoes(self):
    nome_fruta_ou_legume = input("Qual é o nome da fruta ou legume selecionado? ")
    if fruta_ou_legume == "F":
      print("Fruta:", nome_fruta_ou_legume)
    elif fruta_ou_legume == "L":
      print("Legume:", nome_fruta_ou_legume)
 
 
feira = FeiraLivre(["Maçã", "Banana", "Laranja", "Abacaxi", "Manga"], ["Abobrinha", "Batata", "Berinjela", "Cenoura"])
 
# MAIN
feira.imprimir_lista()
fruta_ou_legume = feira.solicitar_fruta_ou_legume()
feira.imprimir_informacoes()

##-------##


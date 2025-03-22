
descricao = """
gosta de filmes de ação
"""

nome = "Guilherme"


print(descricao)

#Procurando palavra na descrição
print("gosta" in descricao)

#Fatiando palavra
print(nome[1:7])

#Fatiando por passo determinado - de 2 em 2
print(nome[0:9:2])

#Invertendo string
print(nome[::-1])

#Metodos em string
print(nome.upper())
print(nome.lower())
print(nome.find("e")) #Mostra a posição das letras na palavra
#Elevando um numero ao quadrado, nessa função ela recebe como uma variavel.
potencia = lambda numero: numero ** 2
print(potencia(4))

verificar_par = lambda numero: numero % 2 == 0
print(verificar_par(4))
print(verificar_par(7))

dividir_por_outro = lambda numero1, numero2: numero1 / numero2
print(dividir_por_outro(25, 5))

reverter_string = lambda palavra: palavra[::-1]
print(reverter_string("Guilherme"))
print(reverter_string("subi no onibus"))

#lista de filmes e dicionario com notas
lista_de_filmes = ["Interestelar", "O regresso", "Oppenheimer", "Mulher Maravilha 1984"]
notas_filmes = {"Interestelar": [9.3, 6.9, 10.0, 8.2],
                "O regresso": [8.3, 8.0, 9.0, 7.2],
                "Oppenheimer": [9.8, 9.9, 7.0, 8.2],
                "Mulher Maravilha 1984": [8.3, 7.0, 8.2, 4.2]
                }

#Descobrindo a media dos filmes
media_notas_filmes = lambda nome: sum(notas_filmes[nome])/ len(notas_filmes[nome])
print(f"Média de avaliação - {media_notas_filmes('Interestelar')}")

#Verificando se o filme existe na lista
verifica_filme = lambda nome_filme: nome_filme in lista_de_filmes
print(verifica_filme('O regresso'))
print(verifica_filme('Joker'))
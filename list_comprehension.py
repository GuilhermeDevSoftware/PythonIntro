# listando 0 a 9 em uma lista
# listNumber = [i for i in range(10)]

#Introduzindo lógica, mostrando 0 a 3
listNumber = [i for i in range(10) if i < 4]
print(listNumber)

#lista de filmes
filme_lista = ["Alladin", "Interestelar", "Tenet", "Batman"]

#Conferindo filmes que tem a letra 'e' na palavra
filme_contem_e = [movie for movie in filme_lista if 'e' in movie.lower()]
print(filme_contem_e)

#Verificando se ja assistiu determinado filme
filme_assistido = [movie for movie in filme_lista if movie != "Tenet"]
print(filme_assistido)

#Verificando se o filme existe
while True:
    filme_procura = input("Digite o nome do filme desejado ou 'sair' para cancelar: ")
    if filme_procura.lower() == 'sair':
        print("Saindo da lista.")
        break

    filme_achado = [movie for movie in filme_lista if filme_procura.lower() in movie.lower()]
    if filme_achado:
        print(f"Filme {filme_procura} encontrado.")
        for movie in filme_achado:
            print(movie)
    else:
        print(f"Nenhum filme encontrado {filme_achado}")

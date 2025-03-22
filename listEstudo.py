filme = [] #lista

print(type(filme))

filmePotter = ["Harry Potter", 1999, 9.3, True]

#print(filmePotter)

filmeList = ["Senhor dos Aneis", "Interestelar", "Perdido em Marte", "Batman", "A Ressaca"]

#print(filmeList[:2]) #Mostrando apenas dois filmes
#print(filmeList[-1]) #Mostrando o ultimo
#print(filmeList[1:4:2])

print(len(filmeList)) #Verificando o tamanho da lista
print(filmeList.index("Perdido em Marte")) #Procurando posicao do filme pelo nome

filmeList.append("Deadpool") #Adicionando filme a lista

print(filmeList)

filmeList.sort() #Ordenando de forma alfabetica
print(filmeList)

#Copiando dados da lista para outra lista e removendo
Filme_copy = filmeList.copy()
Filme_copy.remove("Batman")
Filme_copy.append("O poço")
Filme_copy.append("Aladin")
Filme_copy.sort()

print(Filme_copy)
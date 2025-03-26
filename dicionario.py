filmeJoker = {
    "titulo" : "Joker",
    "Ano" : 2019,
    "Nota" : 8.7,
    "Genero" : ["Ação", "Drama"] #Aqui estou usando uma lista dentro de um dicionario
}

print(type(filmeJoker))
print(filmeJoker)

print(len(filmeJoker))

#Buscando informação 
print(filmeJoker["Genero"])
print(filmeJoker.get("Nota"))

#Buscando as chaves do dicionario
print(filmeJoker.keys())

#Buscando os valores
print(filmeJoker.values())

#Buscando todos os valores
print(filmeJoker.items())

#Adicionando itens
filmeJoker["Diretor"] = "Todd Philipps"
print(filmeJoker)

#Atualizando valores
filmeJoker.update({"Nota" : 9.2})
print(filmeJoker)

#Removendo valores
filmeJoker.pop("Diretor")
print(filmeJoker)

filmeJoker["Diretor"] = "Allan"
print(filmeJoker)
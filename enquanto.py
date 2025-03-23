lista_filme = ["Bob esponja", "Tenet", "A origem", "A espera de um milagre"]

index = 0

#Mostrando a lista pelo while
# while index < len(lista_filme):
#     print(lista_filme[index])
#     index += 1

#Parando em um filme definido
# while index < len(lista_filme):
#     if lista_filme[index] == "A origem":
#         break
#     print(lista_filme[index])
#     index += 1


#Parando em um filme definido
while index < len(lista_filme):
    if lista_filme[index] == "Tenet":
        continue
    print(lista_filme[index])
    index += 1
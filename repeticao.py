# lista_filme = ["Interestelar", "O poderoso chefão", "Coringa", "Bee Movie"]

# #iterando cada filme na lista
# for nome in lista_filme:
#     print(nome)

dicionario_filme = {
    "Interestelar" :{
        "Ano" : 2018,
        "Nota" : 9.3,
        "Diretor" : "Cristopher Nolan"
    },
    "Tenet" :{
        "Ano" : 2021,
        "Nota" : 9.0,
        "Diretor" : "Cristopher Nolan"
    },
    "Batman: O Cavaleiro das Trevas" :{
        "Ano" : 2012,
        "Nota" : 7.9,
        "Diretor" : "Cristopher Nolan"
     },
     "Bob Esponja" : {
         "Ano" : 2015,
         "Nota" : 8.6,
         "Diretor" : "Keanu Reaves"
     }

}

#Mostrando nome e nota, aqui percorro o dicionario
#for nome in dicionario_filme:
#    nota = dicionario_filme[nome]["Nota"]
#    print(f"{nome} -- Nota: {nota}")

#Aqui estou encontrando uma palavra e parando quando a encontra
# for nome in dicionario_filme:
#     diretor = dicionario_filme[nome]["Diretor"]
#     if nome == "Bob Esponja":
#         break
#     print(f"{nome} -- {diretor}")

nome_filme = input("Digite o nome do filme: ")
quantidade_nota = int(input("Digite a quantidade de avaliações que o filme terá: "))

controle = 0

for i in range(quantidade_nota):
    nota = float(input("Digite a nota do filme: "))
    controle += nota

if quantidade_nota > 0:
    media = controle / quantidade_nota
    print(f"A media do filme {nome_filme} e {media:.2f}")
else:
    print("Filme não avaliado")    
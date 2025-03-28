import pprint

filmesDic = {
    "Joker" :{
        "Ano" : 2019,
        "Nota" : 8.7,
        "Genero" : ["Ação", "Drama"]
    }, 
    "Batman" :{
        "Ano" : 2012,
        "Nota" : 8.0,
        "Genero" : ["Suspense", "Ação", "Drama"]
    },
    "Interestelar" :{
        "Ano" : 2018,
        "Nota" : 9.3,
        "Genero" : ["Sci-fi", "Ação"]
    }
}

#Deixa mais legivel no terminal
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmesDic)

#Buscando informação
print(filmesDic["Joker"]["Nota"])

#Adicionando valor
filmesDic["Interestelar"]["Diretor"] = "Cristopher Nolan"
pp.pprint(filmesDic)

#Removendo item
del filmesDic["Batman"]
pp.pprint(filmesDic)

#Removendo apenas um item do dicionario aninhado
filmesDic["Joker"].pop("Nota")
pp.pprint(filmesDic)
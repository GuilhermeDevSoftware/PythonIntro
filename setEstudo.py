filmeSet = {"Senhor dos Aneis", "Interestelar", "Perdido em Marte", "Batman", "A Ressaca"}

print(type(filmeSet))

exemploSet = {"A Origem"}

#Aqui o filme Set recebe os dados de exemplo set, se forem dados iguais, ele não duplica
filmeSet.update(exemploSet)
print(filmeSet)

#Removendo dados
filmeSet.remove("Senhor dos Aneis")
print(filmeSet)
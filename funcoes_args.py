"""
    * - args - utilizamos quando não temos certeza de quanto parametros queremos ter numa função.
    ** - kwargs - alem dos valores, podemos passar sua respectiva chave
"""

#soma de numero
def sum(*num):
    soma_total = 0
    for n in num:
        soma_total += n
    print(f"Soma total: {soma_total}")    

sum(5, 4, 9, 2) 

#apresentacao de curso
def apresentacao_curso(**dicionario_curso):
    for chave, valor in dicionario_curso.items():
        print(f"{valor} - {chave}")

print("Apresentação de curso: ")
apresentacao_curso(nome = "Python for data", category = "Data cience", nivel = 3)
apresentacao_curso(nome = "C++ for systens embarccad", category = "Eletronic", nivel = 4)
apresentacao_curso(nome = "Javascrit for web developers", category = "Web Design", nivel = 1)
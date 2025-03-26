def nome_completo(nome, sobrenome):
    print(f"{nome} {sobrenome}")

nome_completo("Fulano", "Silva")    
nome_completo("Jose", "Treco")

def funcao_soma_dois_numero(a, b):
    return(a + b)

print(f"Soma - {funcao_soma_dois_numero(5,5)}")

#parametro defaul
def endereco(pais = "Brasil"):
    print(f"Eu moro no {pais}")

endereco()    
endereco("Suiça")

def avaliar_filme(qtd_nota, nome_filme):
    total = 0
    for i in range(qtd_nota):
        nota = float(input("Nota: "))
        total += nota

    if nota > 0:
        media = total / qtd_nota

    else:
        media = 0

    print(f"O filme {nome_filme} tem nota {media:.2} de media")

avaliar_filme(2, "Dracula")                
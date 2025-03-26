#função para imprimir mensagem

def bem_vindo():
    print("Seja bem vindo!")

bem_vindo()    

# for i in range(10):
#     bem_vindo()

def calcula_media():
    qtd_nota = int(input("quantidade de notas: "))
    total = 0

    for i in range(qtd_nota):
        nota = float(input("Nota: "))
        total += nota

    if nota > 0:
        media = total / qtd_nota

    else:
        print("Filme sem avaliação.")
        media = 0
    return media      

#print(f"A media de avaliações: [{calcula_media():.2f}]")

#função para cadastro
def create():
    nome = input("Digite o nome do filme: ")
    ano_de_lancamento = int(input("Digite o ano de lançamento do filme: "))
    preco = float(input("Digite o preço do filme: "))
    nota_do_filme = float(input("Digite a nota do filme: "))

    print(f"{nome} -- Lançamento: {ano_de_lancamento} -- preco: {preco:.2f} -- Avaliação: {nota_do_filme}.")

create()
create()
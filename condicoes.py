# nome = input("Digite o nome do filme: ")
# ano = int(input("Digite o ano de lançamento do filme: "))
# nota = float(input("Digite a nota do filme: "))

# if nota > 7.5 and ano > 2018:
#     print(f"O filme {nome}é muito bom! Recomendo")
# else:
#     print(f"O filme {nome}não é bom..")    

num1 = float(input("Digite o primeiro numero: \n"))
num2 = float(input("Digite o segundo numero: \n"))

operacao = input("Digite a operação (+) (-) (*) (/): ")

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2  
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro! Não é possivel dividir um numero por zero.")
        resultado = 0
else:
    print("Digite uma operação valida.")

print(f"Resultado da operação: {resultado:.2f}")
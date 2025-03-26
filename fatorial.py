def fatorial(num):
    if num == 1:
        return 1
    else: 
        return (num * fatorial(num -1))
    

numero = int(input("Digite o numero para o fatorial: "))
print(f"Fatorial de {numero} -- {fatorial(numero)}")    

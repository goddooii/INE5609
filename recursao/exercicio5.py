def somaAteN(n,soma=0):
    if n != 0:
        soma = soma + n
        return somaAteN(n-1,soma)
    return soma
    
print(somaAteN(int(input())))
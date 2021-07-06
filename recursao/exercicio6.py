def maiorElemento(lista, maior):
    if len(lista) > 0:
        maiorAtual = lista.pop()
        if maiorAtual > maior:
            maior = maiorAtual
        return maiorElemento(lista, maior)
    return maior

lista = [int(i) for i in input().split()]
print(maiorElemento(lista, lista.pop()))
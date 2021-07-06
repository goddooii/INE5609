def contaCaracteresPorUnidade(texto, qtd=0):
    if (texto != ''): 
        return contaCaracteresPorUnidade(texto[1:], qtd+1)
    return qtd

print(contaCaracteresPorUnidade(input()))
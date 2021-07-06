def imprimeTextoInvertidoPorChar(texto):
    if (texto != ''):
        print(texto[-1:])
        return imprimeTextoInvertidoPorChar(texto[:-1])
    return
    
imprimeTextoInvertidoPorChar(input())
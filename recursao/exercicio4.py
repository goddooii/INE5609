def verificaSequenciaCresc(seq):
    if len(seq) > 2:
        if seq.pop(0) < seq[0]:
            return verificaSequenciaCresc(seq)
        return False
    return seq[0] < seq[1]
    
print(verificaSequenciaCresc(input().split()))
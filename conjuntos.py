conjunto_checagem = []

def cojunto_potencia(conj_p):
    for conj in conj_p:

        if not conj:
            if "[Ø]" in conjunto_checagem:
                continue
            print("[Ø]")
            conjunto_checagem.append("[Ø]")
            continue
        elif conj[::-1] in conjunto_checagem:
            continue
        elif conj[0] == conj[1]:
            if conj[0] and conj[1] in conjunto_checagem:
                continue
            else:
                print("[" + str(conj[0]) + "]")
                conjunto_checagem.append(conj[0])
        else:
            print(conj)
            conjunto_checagem.append(conj)


conjuntos = sorted([[], [], [5, 2], [1, 2], [2, 1], [3, 4], [1, 1], [5, 5], [5, 5], [3, 2], [5, 3, 1]])

cojunto_potencia(conjuntos)

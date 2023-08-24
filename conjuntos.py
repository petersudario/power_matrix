conjunto_checagem = []

def cojunto_potencia(lst):
    seen = set()  # To keep track of printed subsets
    for subset in lst:
        if tuple(subset) not in seen:
            seen.add(tuple(subset))
            print(subset)



conjuntos = sorted([[], [], [5, 2], [1, 2], [2, 1], [3, 4], [1, 1], [5, 5], [5, 5], [3, 2], [5, 3, 1]])

cojunto_potencia(conjuntos)

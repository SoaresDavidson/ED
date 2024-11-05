from algoritmos import insertionSort,bubble_sort

nomes50k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes50k.txt"
nomes100k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes100k.txt"
nomes250k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes250k.txt"
nomes500k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes500k.txt"
nomes1000k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes1000k.txt"

with open(nomes50k) as lista:
    arr_insertion = lista.readlines()
    arr_bubble = arr_insertion.copy()
    arr_selection = arr_insertion.copy()

    tempo_insertion = insertionSort(arr_insertion)
    tempo_bubble = bubble_sort(arr_bubble)
    #tempo_selection = selectionSort(arr_selection)
    
    print(f"insertion levou {tempo_insertion} segundos")
    print(f"heap levou {tempo_bubble} segundos")
    #print(f"selection levou {tempo_selection} segundos")
from algoritmos import quick,merge_sort,heapSort

nomes50k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes50k.txt"
nomes100k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes100k.txt"
nomes250k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes250k.txt"
nomes500k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes500k.txt"
nomes1000k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes1000k.txt"

with open(nomes1000k) as lista:
    arr_quick = lista.readlines()
    arr_merge = arr_quick.copy()
    arr_heap = arr_quick.copy()

    tempo_merge = merge_sort(arr_merge)
    #tempo_quick = quick(arr_quick)
    #tempo_heap = heapSort(arr_heap)
    
    print(f"merge levou {tempo_merge} segundos")
    #print(f"heap levou {tempo_heap} segundos")
    #print(f"quick levou {tempo_quick} segundos")
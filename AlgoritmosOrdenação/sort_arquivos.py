import algoritmos

nomes50k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes50k.txt"
nomes100k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes100k.txt"
nomes250k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes250k.txt"
nomes500k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes500k.txt"
nomes1000k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes1000k.txt"

with open(nomes50k) as lista:
    arr = lista.readlines()
    print(arr)

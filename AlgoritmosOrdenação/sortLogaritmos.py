from algoritmos import quickSort, merge_sort, heapSort, shellSort
import matplotlib.pyplot as plt
import numpy as np
import menu


nomes50k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes50k.txt"
nomes100k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes100k.txt"
nomes250k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes250k.txt"
nomes500k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes500k.txt"
nomes1000k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes1000k.txt"

arquivos = [nomes50k, nomes100k, nomes250k, nomes500k, nomes1000k]

algoritmos = [quickSort, merge_sort, heapSort, shellSort]
tempos = dict()


labels = ['Quick', 'Merge', 'Heap', 'Shell']


tempo_quick = list()
tempo_merge = list()
tempo_heap = list()
tempo_shell = list()


for arquivo in arquivos:
    tempo_quick.append(menu.calcula_media(arquivo, quickSort))
    tempo_merge.append(menu.calcula_media(arquivo, merge_sort))
    tempo_heap.append(menu.calcula_media(arquivo, heapSort))
    tempo_shell.append(menu.calcula_media(arquivo, shellSort))


x = np.arange(len(arquivos))


largura = 0.2

x_quick = x - 1.5 * largura
x_merge = x - 0.5 * largura
x_heap = x + 0.5 * largura
x_shell = x + 1.5 * largura


plt.bar(x_quick, tempo_quick, largura, label='Quick', color='skyblue')
plt.bar(x_merge, tempo_merge, largura, label='Merge', color='lightgreen')
plt.bar(x_heap, tempo_heap, largura, label='Heap', color='lightcoral')
plt.bar(x_shell, tempo_shell, largura, label='Shell', color='orange')

plt.title('Algoritmos de Ordenação - Gráfico de Barras')
plt.xlabel('Algoritmos')
plt.ylabel('Tempo (s)')

plt.xticks(x, ['50k', '100k', '250k', '500k', '1000k'])


plt.legend()


plt.tight_layout()
plt.savefig('grafico_barras_algoritmos.png')  

plt.close()


plt.plot(x, tempo_quick, label='Quick', marker='o', color='skyblue', linewidth=2)
plt.plot(x, tempo_merge, label='Merge', marker='s', color='lightgreen', linewidth=2)
plt.plot(x, tempo_heap, label='Heap', marker='^', color='lightcoral', linewidth=2)
plt.plot(x, tempo_shell, label='Shell', marker='D', color='orange', linewidth=2)


plt.title('Algoritmos de Ordenação - Gráfico de Linhas')
plt.xlabel('Arquivos')
plt.ylabel('Tempo (s)')

plt.xticks(x, ['50k', '100k', '250k', '500k', '1000k'])


plt.legend()

plt.tight_layout()
plt.savefig('grafico_linhas_algoritmos.png')  

plt.close()
print("Os gráficos foram salvos como 'grafico_barras_algoritmos.png' e 'grafico_linhas_algoritmos.png'.")

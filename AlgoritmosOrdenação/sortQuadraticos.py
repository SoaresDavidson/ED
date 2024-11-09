from algoritmos import insertionSort, bubbleSort, selectionSort
import matplotlib.pyplot as plt
import numpy as np
import menu

nomes50k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes50k.txt"
nomes100k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes100k.txt"
nomes250k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes250k.txt"
nomes500k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes500k.txt"
nomes1000k = "AlgoritmosOrdenação/dados-20241102T131234Z-001/dados/nomes1000k.txt"

arquivos = [nomes50k,nomes100k,nomes250k,nomes500k]

tempo_bubble = list()
tempo_insertion = list()
tempo_selection = list()

for arquivo in arquivos:
    tempo_insertion.append(menu.calcula_media(arquivo,insertionSort ))
    tempo_bubble.append(menu.calcula_media(arquivo, bubbleSort))
    tempo_selection.append(menu.calcula_media(arquivo, selectionSort))

tempo_insertion.append(tempo_insertion[len(tempo_insertion)-1] * 4)
tempo_bubble.append(tempo_bubble[len(tempo_bubble)-1] * 4)
tempo_selection.append(tempo_selection[len(tempo_selection)-1] * 4)

x = np.arange(len(arquivos)+1)

largura = 0.2

x_insertion = x - 1.5 * largura
x_selection = x - 0.5 * largura
x_bubble = x + 0.5 * largura

plt.bar(x_insertion, tempo_insertion, largura, label='Insertion', color='skyblue')
plt.bar(x_selection, tempo_selection, largura, label='Selection', color='lightgreen')
plt.bar(x_bubble, tempo_bubble, largura, label='Bubble', color='lightcoral')

plt.title('Algoritmos de Ordenação - Gráfico de Barras')
plt.xlabel('Arquivos')
plt.ylabel('Tempo (s)')

plt.xticks(x, ['50k', '100k', '250k', '500k', '1000k'])
plt.legend()

plt.tight_layout()
plt.savefig('grafico_barras_algoritmos_quadraticos.png')
plt.close()

plt.plot(x, tempo_insertion, label='Insertion', marker='o', color='skyblue', linewidth=2)
plt.plot(x, tempo_selection, label='Selection', marker='s', color='lightgreen', linewidth=2)
plt.plot(x, tempo_bubble, label='Bubble', marker='^', color='lightcoral', linewidth=2)

plt.title('Algoritmos de Ordenação - Gráfico de Linhas')
plt.xlabel('Arquivos')
plt.ylabel('Tempo (s)')

plt.xticks(x, ['50k', '100k', '250k', '500k', '1000k'])
plt.legend()

plt.tight_layout()
plt.savefig('grafico_linhas_algoritmos_quadraticos.png')
plt.close()

print("Os gráficos foram salvos como 'grafico_barras_algoritmos_quadraticos.png' e 'grafico_linhas_algoritmos_quadraticos.png'.")

import matplotlib.pyplot as plt

# Dados fornecidos
algoritmos = ['Merge Sort', 'Quick Sort', 'Heap Sort', 'Shell Sort']
tamanhos = ['100k', '250k', '500k', '1000k']

# Tempos médios (em segundos)
tempos_merge = [0.48, 1.42, 2.84, 6.08]
tempos_quick = [0.45, 1.12, 2.72, 7.90]
tempos_heap = [0.67, 2.08, 4.41, 10.21]
tempos_shell = [0.92, 2.17, 5.20, 11.96]

# Plotagem dos gráficos de linhas
plt.figure(figsize=(10, 6))

plt.plot(tamanhos, tempos_merge, marker='o', label='Merge Sort')
plt.plot(tamanhos, tempos_quick, marker='o', label='Quick Sort')
plt.plot(tamanhos, tempos_heap, marker='o', label='Heap Sort')
plt.plot(tamanhos, tempos_shell, marker='o', label='Shell Sort')

plt.xlabel('Tamanho da lista')
plt.ylabel('Tempo Médio (segundos)')
plt.title('Tempo Médio de Execução por Tamanho da lista')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

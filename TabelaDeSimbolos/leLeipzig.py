import HashTable,TabelaDeSimbolosBuscaBinaria,TabelaDeSimbolosEncadeada
import menu
import matplotlib.pyplot as plt

fileName = "TabelaDeSimbolos/leipzig100k.txt"
tabelas = [HashTable.tabelaHash(227),TabelaDeSimbolosBuscaBinaria.BinarySearchST(),TabelaDeSimbolosEncadeada.TabelaEncadeada()]
tempos = list()
nomes = ['Tabela Hash','Tabela com Busca Binaria', 'Tabela Encadeada']

for tabela in tabelas:
    t = tabela
    tempos.append(menu.calcula_media(fileName,t))

menu.costruir_grafico(nomes,tempos)    




import HashTable,TabelaDeSimbolosBuscaBinaria,TabelaDeSimbolosEncadeada
import menu
import matplotlib.pyplot as plt

fileName = "TabelaDeSimbolos/leipzig100k.txt"
tabelas = [HashTable.tabelaHash,TabelaDeSimbolosBuscaBinaria.BinarySearchST,TabelaDeSimbolosEncadeada.TabelaEncadeada]
parametros = [[227],[],[]]
tempos = list()
nomes = ['Tabela Hash','Tabela com Busca Binaria', 'Tabela Encadeada']

for i,tabela in enumerate(tabelas):
    tempos.append(menu.calcula_media(fileName,tabela, parametros[i],))

#menu.costruir_grafico(nomes,tempos,Xlabel='Tabelas',Ylabel='Tempos (s)',title='Tabelas de Símbolos')    




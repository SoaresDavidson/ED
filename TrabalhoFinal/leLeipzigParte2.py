import menu
import matplotlib.pyplot as plt
tempos = list()
fileName = "TrabalhoFinal/leipzig100k.txt"
tempo = 0
capacity = 271
tabela = [{} for _ in range(capacity)]
tempos.append(menu.calcula_media(arquivo = fileName,tabela = tabela,quant = 5))
print(tempos)
print(tabela[0])
#menu.costruir_grafico(nomes,tempos,Xlabel='Tabelas',Ylabel='Tempos (s)',title='Tabelas de Símbolos')    




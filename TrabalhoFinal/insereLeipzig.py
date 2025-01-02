import menu,collections
import matplotlib.pyplot as plt

tempos = list()
nomes = ["hashTable","Counter","dicionario"]
fileName = "TrabalhoFinal/leipzig100k.txt"

def uso_lista_dict():
    capacity = 271
    tabela = [{} for _ in range(capacity)]
    tempos.append(menu.calcula_media_tables(arquivo = fileName,tabela = tabela))
    #print(tempos)
    return tabela

def uso_Counter():
    counter = collections.Counter()
    tempos.append(menu.calcula_media_counter(arquivo = fileName, tabela = counter))
    #print(counter)
    return counter

def uso_dict():
    tabela = {}
    tempos.append(menu.calcula_media_dict(arquivo = fileName, tabela = tabela))
    #print(tabela)
    return tabela

uso_lista_dict()
uso_Counter()
uso_dict()
print(tempos)

menu.costruir_grafico(nomes,tempos,Xlabel='Tabelas',Ylabel='Tempos (s)',title='Inserção',save_path= "insertTimes.png",directory= "TrabalhoFinal/tempos")  

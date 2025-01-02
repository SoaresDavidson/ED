import menu,collections
import matplotlib.pyplot as plt

tempos = list()
nomes = ["hashTable","Counter","dicionario"]
fileName = "TrabalhoFinal/leipzig100k.txt"

def uso_lista_dict():
    capacity = 271
    tabela = [{} for _ in range(capacity)]
    result = menu.read_from_file_tables(filename = fileName,tabela = tabela)
    #print(tempos)
    return result[1]

def uso_Counter():
    counter = collections.Counter()
    result = menu.read_from_file_counter(filename = fileName, counter = counter)
    #print(counter)
    return result[1]

def uso_dict():
    tabela = {}
    result = menu.read_from_file_dict(filename = fileName, tabela = tabela)
    #print(tabela)
    return result[1]

tabela_lista_dict = uso_lista_dict()
tabela_counter = uso_Counter()
tabela_dict = uso_dict()
print(tempos)

palavras = ["Lisbon", "NASA",
"Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella", "vaccinations", "government",
"Authorities"]

tempos_lista_dict = []
for i in palavras:
    tempo = menu.delete_lista_dict(tabela_lista_dict, i)
    tempos_lista_dict.append(tempo[0] * 10e4)

tempos_counter = []
for i in palavras:
    tempo = menu.delete_dict(tabela_counter, i)
    tempos_counter.append(tempo[0] * 10e4)

tempos_dict = []
for i in palavras:
    tempo = menu.delete_dict(tabela_dict, i)
    tempos_dict.append(tempo[0] * 10e4)

for i in palavras:
    x = menu.busca_lista_dict(tabela_lista_dict, i)
    print(x)

for i in palavras:
    x = menu.busca_dict(tabela_counter, i)
    print(x)

for i in palavras:
    x = menu.busca_dict(tabela_dict, i)
    print(x)

menu.costruir_grafico(palavras, tempos_lista_dict,Xlabel='Tabelas',Ylabel='Tempos (ms)',title='Tempos de Deleção hashtable', save_path= "deleteTimesListDict.png",directory= "TrabalhoFinal/tempos") 
menu.costruir_grafico(palavras, tempos_counter,Xlabel='Tabelas',Ylabel='Tempos (ms)',title='Tempos de Deleção counter', save_path= "deleteTimesCounter.png",directory= "TrabalhoFinal/tempos") 
menu.costruir_grafico(palavras, tempos_dict,Xlabel='Tabelas',Ylabel='Tempos (ms)',title='Tempos de Deleção  dicionario', save_path= "deleteTimesDict.png",directory= "TrabalhoFinal/tempos") 
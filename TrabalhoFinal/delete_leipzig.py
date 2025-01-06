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

def uso_tupla_dict():
    capacity = 271
    tabela = tuple({} for _ in range(capacity))
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
tabela_tupla_dict = uso_tupla_dict()
tabela_counter = uso_Counter()
tabela_dict = uso_dict()
print(tempos)

palavras = ["Lisbon", "NASA",
"Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella", "vaccinations", "government",
"Authorities"]

media = 5

tempos_lista_dict = []
for i in palavras:
    sum = 0
    for _ in range(media):
        aux = [_.copy() for _ in tabela_lista_dict]
        tempo = menu.delete_lista_dict(aux, i)
        #print("lista_dict",tempo[1], i)
        sum += tempo[0]
    tempos_lista_dict.append((sum/media) * 1e6)

tempos_tupla_dict = []
for i in palavras:
    sum = 0
    for _ in range(media):
        aux = tuple(_.copy() for _ in tabela_tupla_dict)
        tempo = menu.delete_lista_dict(aux, i)
        #print("lista_dict",tempo[1], i)
        sum += tempo[0]
    tempos_tupla_dict.append((sum/media) * 1e6)

tempos_counter = []
for i in palavras:
    sum = 0
    for _ in range(media):
        aux = tabela_counter.copy()
        tempo = menu.delete_dict(aux, i)
        #print("counter",tempo[1], i)
        sum += tempo[0]
    tempos_counter.append((sum/media) * 1e6)

tempos_dict = []
for i in palavras:
    sum = 0
    for _ in range(media):
        aux = tabela_dict.copy()
        tempo = menu.delete_dict(aux, i)
        #print("dicionario",tempo[1], i)
        sum += tempo[0]
    tempos_dict.append((sum/media) * 1e6)

menu.costruir_grafico(palavras, tempos_lista_dict,Xlabel='Tabelas',Ylabel='Tempos (µs)',title='Tempos de Deleção hashtable', save_path= "deleteTimesListDict.png",directory= "TrabalhoFinal/tempos") 
menu.costruir_grafico(palavras, tempos_tupla_dict,Xlabel='Tabelas',Ylabel='Tempos (µs)',title='Tempos de Deleção hashtable com tupla', save_path= "deleteTimesTupleDict.png",directory= "TrabalhoFinal/tempos") 
menu.costruir_grafico(palavras, tempos_counter,Xlabel='Tabelas',Ylabel='Tempos (µs)',title='Tempos de Deleção counter', save_path= "deleteTimesCounter.png",directory= "TrabalhoFinal/tempos") 
menu.costruir_grafico(palavras, tempos_dict,Xlabel='Tabelas',Ylabel='Tempos (µs)',title='Tempos de Deleção dicionario', save_path= "deleteTimesDict.png",directory= "TrabalhoFinal/tempos") 
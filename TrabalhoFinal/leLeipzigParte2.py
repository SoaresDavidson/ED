import menu,collections
import matplotlib.pyplot as plt

tempos = list()
fileName = "TrabalhoFinal/leipzig100k.txt"

def uso_lista_dict():
    capacity = 271
    tabela = [{} for _ in range(capacity)]
    tempos.append(menu.calcula_media_tables(arquivo = fileName,tabela = tabela))
    print(tempos)

def uso_Counter():
    counter = collections.Counter()
    tempos.append(menu.read_from_file_counter(filename = fileName, counter = counter))

    print(counter)

def uso_dict():
    tabela = {}
    tempos.append(menu.read_from_file_dict(filename = fileName, tabela = tabela))
    print(tabela)

uso_lista_dict()
uso_Counter()
uso_dict()
print(tempos)

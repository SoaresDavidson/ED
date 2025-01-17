import time,re,random,os,json,collections
import matplotlib.pyplot as plt

def conta_tempo(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        result = func(*args,**kwargs)
        t2 = time.perf_counter() - t1
        #print(t2)
        return [t2,result]
    return wrapper

@conta_tempo
def read_from_file_tables(filename:str,tabela, value: int = 0) -> None:
    try:
        with open(filename, 'r',encoding="utf-8") as file:
            for line in file:
                words = line.split()
                for word in words:
                    new_word = clean_word(word)
                    addHash(tabela, new_word, value)
        return tabela 
        #save_to_file(tabela.__class__.__name__+'.txt',tabela)        
    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")
        
@conta_tempo 
def read_from_file_counter(filename:str, counter) -> None:
    try:
        with open(filename, 'r',encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            counter.update(filter(clean_word, words))
        #save_to_file(tabela.__class__.__name__+'.txt',tabela)
        return counter        
    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")

@conta_tempo 
def read_from_file_dict(filename:str, tabela:dict, value:int = 0) -> None:
    try:
        with open(filename, 'r',encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            for word in words:
                tabela[clean_word(word)] = value
        #save_to_file(tabela.__class__.__name__+'.txt',tabela) 
        return tabela        
    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")

def _hash(key, capacity): 
        return hash(key) % capacity

def addHash(tabela:list, key, value):
    listKey = _hash(key, len(tabela))
    tabela[listKey][key] = value

def clean_word(word:str) -> str:
    return re.sub(r"(?<![a-zA-Z])'|'(?![a-zA-Z])|(?<![a-zA-Z0-9])[^\w']+|[^\w']+(?![a-zA-Z0-9])", "", word)

filter

def save_to_file(filename: str, tabela,directory="TabelaDeSimbolos/arquivos_salvos"):

    try:
        os.makedirs(directory, exist_ok=True) 
        file_path = os.path.join(directory, filename)
        if os.path.exists(file_path):
            print(f"O arquivo '{file_path}' já existe. Salvamento ignorado.")
            return
        with open(file_path, 'w') as file:
            file.write(tabela.__str__())
        print(f"Tabela salva em '{filename}'.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

import os
import json

def save_times(filename: str,tipo:str, tempos, directory="TrabalhoFinal/arquivos_salvos") -> None:
    try:
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
        else:
            data = {}
        data[tipo] = tempos 
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Tabela salva em '{filename}' no formato JSON.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


def calcula_media_tables(arquivo:str,tabela, quant:int = 5) -> int:
    sum = 0
    for i in range(quant):
        new_tabela = tabela
        tempo = read_from_file_tables(arquivo, new_tabela)
        sum += tempo[0]
    #save_times('Tempos.json',tabela.__name__+'.json',tempos)    
    return sum/quant

def calcula_media_counter(arquivo:str,tabela:collections.Counter , quant:int = 5) -> int:
    sum = 0
    for i in range(quant):
        new_tabela = tabela
        tempo = read_from_file_counter(arquivo, new_tabela)
        sum += tempo[0]
    #save_times('Tempos.json',tabela.__name__+'.json',tempos)    
    return sum/quant

def calcula_media_dict(arquivo:str,tabela, quant:int = 5) -> int:
    sum = 0
    for i in range(quant):
        new_tabela = tabela
        tempo = read_from_file_dict(arquivo, new_tabela)
        sum += tempo[0]
    #save_times('Tempos.json',tabela.__name__+'.json',tempos)    
    return sum/quant

@conta_tempo
def busca_lista_dict(tabela:list,key):
    hashKey = _hash(key, len(tabela))
    try:
        return tabela[hashKey][key]
    except:
        return None
    
@conta_tempo
def busca_dict(tabela:list,key):
    try:
        return tabela[key]
    except:
        return None
    
@conta_tempo
def delete_lista_dict(tabela:list, key):
    hashKey = _hash(key, len(tabela))
    try:
        aux = tabela[hashKey][key]
        del tabela[hashKey][key]
        return aux
    except:
        return None
    
@conta_tempo
def delete_dict(tabela:list,key):
    try:
        aux = tabela[key]
        del tabela[key]
        return aux
    except:
        return None


def costruir_grafico(x, y, Xlabel: str, Ylabel: str, title: str, Bar: bool = True, save_path: str = "grafico_tabelas.png", directory: str = "arquivos_salvos"):
    cores = ['#FF6F61','#6B8E23','#4B8E8D','#FFD700','#8A2BE2',
                '#FF6347','#20B2AA','#F08080', '#48C9B0' ,'#D3D3D3']
    plt.figure(figsize=(10, 6))
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(Xlabel, fontsize=12)
    plt.ylabel(Ylabel, fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    
    if Bar:
        colors = [cores[i % len(cores)] for i, _ in enumerate(x)]
        bars = plt.bar(x, y, color=colors)
        plt.xticks(rotation=45, ha='right') 
        for bar, label in zip(bars, x):
            plt.text(
                bar.get_x() + bar.get_width() / 2, 
                bar.get_height() + 0.01,
                f'{bar.get_height():.2f}',
                ha='center',
                fontsize=9
            )    
        plt.legend(bars, x, title="Tabelas", bbox_to_anchor=(1.05, 1), loc='upper left')
    else:
        media = sum(y)/len(x)
        bars = plt.bar(x, y, color="skyblue")
        for bar, label in zip(bars, x):
            plt.text(
                bar.get_x() + bar.get_width() / 2, 
                bar.get_height() + 0.05,
                f'{bar.get_height():.2f}',
                ha='center',
                fontsize=9
            )    
        plt.axhline(y=media, color='red', linestyle='-', label=f'Média: {media:.2f}', linewidth=0.8)
        plt.legend()
        #plt.xticks([0, x[-1]], fontsize=10)
        
   
    plt.tight_layout() 
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, save_path)
    plt.savefig(file_path, dpi=300, bbox_inches='tight')  
    print(f"Gráfico salvo em: {file_path}")
    plt.show()

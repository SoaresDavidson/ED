import time,re,random,os,json
import matplotlib.pyplot as plt

def conta_tempo(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time() - t1
        #print(t2)
        return t2
    return wrapper

@conta_tempo
def read_from_file(filename:str, tabela:object, value: int = 0):
    try:
        with open(filename, 'r',encoding="utf-8") as file:
            for line in file:
                words = line.split()
                for word in words:
                    cleaned_word = clean_word(word)
                    if clean_word != '':
                        tabela.put(cleaned_word, value) 
        save_to_file(tabela.__class__.__name__+'.txt',tabela)        
    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")

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

def save_times(filename: str,tipo:str, tempos, directory="TabelaDeSimbolos/arquivos_salvos") -> None:
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

def calcula_media(arquivo:str,tabela, args:list = [], quant:int = 5) -> int:
    sum = 0
    tempos = list()
    for i in range(quant):
        t = tabela(*args)
        tempo = read_from_file(arquivo, t)
        sum += tempo
        tempos.append(tempo)
    save_times('Tempos.json',tabela.__name__+'.json',tempos)    

    return sum/quant

def clean_word(word:str) -> str:
    return re.sub(r"(?<![a-zA-Z])'|'(?![a-zA-Z])|(?<![a-zA-Z0-9])[^\w']+|[^\w']+(?![a-zA-Z0-9])", "", word)

def costruir_grafico(x, y, Xlabel: str, Ylabel: str, title: str, Bar: bool = True, save_path: str = "grafico_tabelas.png", directory: str = "TabelaDeSimbolos/arquivos_salvos"):
    
    plt.figure(figsize=(10, 6))
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(Xlabel, fontsize=12)
    plt.ylabel(Ylabel, fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    
    if Bar:
        colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in x]
        bars = plt.bar(x, y, color=colors) 
        for bar, label in zip(bars, x):
            plt.text(
                bar.get_x() + bar.get_width() / 2, 
                bar.get_height() + 0.05,
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
        plt.xticks([0, x[-1]], fontsize=10)
        
   
    plt.tight_layout() 
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, save_path)
    plt.savefig(file_path, dpi=300, bbox_inches='tight')  
    print(f"Gráfico salvo em: {file_path}")
    plt.show()

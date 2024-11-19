import time,re,random,os
import matplotlib.pyplot as plt

def conta_tempo(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time() - t1
        print(t2)
        return t2
    return wrapper
#
@conta_tempo
def read_from_file(filename:str, tabela, value: int = 0):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    cleaned_word = clean_word(word)
                    tabela.put(cleaned_word, value) 
        #save_to_file(tabela.__class__.__name__,tabela.arr)            
    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")

def realiza_operacao(arquivo:str, tabela) -> float:
    return read_from_file(arquivo,tabela)
'''
def save_to_file(filename: str, arr,directory="TabelaDeSimbolos/arquivos_salvos"):
    try:
        os.makedirs(directory, exist_ok=True) 
        file_path = os.path.join(directory, filename)
        with open(file_path, 'w') as file:
            for item in arr:
                file.write(f"{item.key}: {item.value}\n")
        print(f"Tabela salva em '{filename}'.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
        '''


def clean_word(word):
    return re.sub(r"(?<![a-zA-Z])'|'(?![a-zA-Z])|(?<![a-zA-Z0-9])[^\w']+|[^\w']+(?![a-zA-Z0-9])", "", word)

def calcula_media(arquivo:str,tabela, quant:int = 5):
    sum = 0
    for i in range(quant):
        sum += realiza_operacao(arquivo, tabela)
    return sum/quant

def costruir_grafico(x, y, Xlabel:str,Ylabel:str,title:str,Bar:bool=True, save_path="grafico_tabelas.png",directory="TabelaDeSimbolos/arquivos_salvos"):
    
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
        media = sum(y)/len(y)
        plt.bar(x, y, color="skyblue")
        plt.axhline(y=media, color='red', linestyle='-', label=f'Média: {media:.2f}', linewidth=0.8)
        plt.xticks([0, x[-1]], fontsize=10)
        
    plt.tight_layout() 
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, save_path)
    plt.savefig(file_path, dpi=300, bbox_inches='tight')  
    print(f"Gráfico salvo em: {file_path}")
    plt.show()
import HashTable,TabelaDeSimbolosBuscaBinaria,time,re

def conta_tempo(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time() - t1
        print(t2)
        return t2
    return wrapper

@conta_tempo
def read_from_file(filename, tabela):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    cleaned_word = clean_word(word)
                    tabela.put(cleaned_word, 0) 
    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")


def save_to_file(filename, arr):
    try:
        with open(filename, 'w') as file:
            for item in arr:
                file.write(f"{item.key}: {item.value}\n")
        print(f"Tabela salva em '{filename}'.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


def clean_word(word):
    return re.sub(r"(?<![a-zA-Z])'|'(?![a-zA-Z])|(?<![a-zA-Z0-9])[^\w']+|[^\w']+(?![a-zA-Z0-9])", "", word)

tabela = HashTable.tabelaHash(227)
#tabela = TabelaDeSimbolosBuscaBinaria.BinarySearchST()

read_from_file("TabelaDeSimbolos/leipzig100k.txt", tabela)



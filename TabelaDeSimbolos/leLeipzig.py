import HashTable,TabelaDeSimbolosBuscaBinaria,TabelaDeSimbolosEncadeada ,time,re

def conta_tempo(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time() - t1
        print(t2)
        return t2
    return wrapper

@conta_tempo
def read_from_file(filename, tabela, value = 0):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    cleaned_word = clean_word(word)
                    tabela.put(cleaned_word, value) 
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
#tabela = TabelaDeSimbolosEncadeada.Tabela()


read_from_file("TabelaDeSimbolos/leipzig100k.txt", tabela)



# print(tabela.countByCapacity())
# [415, 405, 376, 418, 386, 409, 432, 421, 389, 389, 405, 412, 402, 395, 433, 448, 417, 435, 423, 394, 410, 386, 420, 440, 421, 423, 403, 372, 427, 407, 438, 407, 425, 405, 404, 425, 413, 394, 366, 385, 368, 416, 
#  416, 409, 413, 398, 406, 375, 394, 420, 429, 406, 394, 421, 422, 399, 399, 362, 377, 390, 417, 419, 408, 396, 416, 376, 430, 413, 378, 414, 421, 382, 423, 420, 363, 420, 419, 412, 401, 404, 393, 411, 435, 392, 
#  403, 437, 442, 370, 399, 428, 421, 395, 378, 391, 412, 400, 378, 369, 390, 395, 404, 393, 398, 416, 390, 416, 409, 384, 419, 425, 376, 426, 413, 390, 373, 398, 424, 420, 405, 408, 442, 400, 415, 392, 393, 424, 
#  384, 382, 375, 369, 411, 400, 417, 373, 406, 419, 414, 383, 418, 394, 398, 401, 437, 388, 409, 409, 411, 392, 409, 425, 434, 426, 401, 414, 398, 395, 409, 433, 388, 424, 401, 394, 430, 418, 398, 382, 380, 453, 
#  393, 419, 388, 418, 414, 413, 384, 360, 397, 410, 474, 440, 401, 398, 397, 377, 441, 410, 431, 400, 404, 
#  393, 421, 417, 376, 440, 400, 415, 407, 382, 388, 413, 368, 424, 417, 384, 386, 415, 423, 420, 384, 413, 
#  412, 421, 390, 348, 406, 427, 410, 415, 382, 411, 391, 406, 389, 411, 414, 420, 393]
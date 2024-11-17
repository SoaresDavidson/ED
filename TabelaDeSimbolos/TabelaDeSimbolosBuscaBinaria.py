import re
class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'({self.key}: {self.value})'


class BinarySearchST:
    def __init__(self):
        self.arr = []

    def __repr__(self):
        return f"BinarySearchST({self.arr})"

    def put(self, k, value=0):
        index = self.find(k,self.arr)
        if index < len(self.arr) and self.arr[index].key == k:
            return
        self.arr.insert(index, Item(k,value)) 

    def find(self, k, arr):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (r + l) // 2
            if arr[mid].key < k:
                l = mid + 1
            elif arr[mid].key > k:
                r = mid - 1
            else:
                return mid
        return l

    def clean_word(self, word):
        return re.sub(r"(?<![a-zA-Z])'|'(?![a-zA-Z])|(?<![a-zA-Z0-9])[^\w']+|[^\w']+(?![a-zA-Z0-9])", "", word)

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for item in self.arr:
                    file.write(f"{item.key}: {item.value}\n")
            print(f"Tabela salva em '{filename}'.")
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")


if __name__ == "__main__":
    tabela = BinarySearchST()
    tabela.read_from_file("TabelaDeSimbolos/leipzig100k.txt")
    tabela.save_to_file("TabelaDeSimbolos/tabela_salva.txt")

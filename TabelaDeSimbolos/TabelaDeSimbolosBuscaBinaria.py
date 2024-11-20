import re
import menu
class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'({self.key}: {self.value})'


class BinarySearchST:
    def __init__(self):
        self.arr = []

    def __str__(self):
        msg = ''
        for element in self.arr:
            msg += f'({element.key} : {element.value})' + '\n'
        return f'tabelaBuscaBinaria: ' + '\n' + msg    

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



if __name__ == "__main__":
    tabela = BinarySearchST()
    menu.read_from_file("TabelaDeSimbolos/leipzig100k.txt",tabela)
    tabela.save_to_file("TabelaDeSimbolos/tabela_salva.txt")
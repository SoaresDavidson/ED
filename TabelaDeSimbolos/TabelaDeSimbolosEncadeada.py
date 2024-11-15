class Node:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.next = None

class Tabela:
    def __init__(self):
        self.ini = None
        self.valor = 0
    
    def put(self, chave):
        if self.ini is None: 
            self.ini = Node(chave, 0)
            self.valor = 1
        else:
            n = self.ini
            while n.next is not None:
                if n.chave == chave: 
                    n.valor = self.valor
                    self.valor += 1
                    return False
                n = n.next
            n.next = Node(chave, self.valor)
            self.valor += 1
            return True
    
    def __str__(self):
        res = ""
        n = self.ini
        while n is not None:
            res += '"' + n.chave + '": ' + str(n.valor)
            if n.next is not None: res += '; '
            n = n.next
        return res

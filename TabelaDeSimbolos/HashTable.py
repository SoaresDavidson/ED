class Hash:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'({self.key}: {self.value})'

class tabelaHash:
    def __init__(self, M):
        self.M = M
        self.n = 0
        self.table = [None] * M


    def __str__(self):
        msg = ''
        for pos in self.table:
            n = pos
            while n is not None:
                msg += (f'({n.key} : {n.value})' + '\n')
                n = n.next
        return f'Tabela Hash: ' + '\n' + msg

    def _hash(self, key): 
        return hash(key) % self.M 


    def put(self, key, value):
        listKey = self._hash(key)
        repeatedHash = self.search(key)

        if repeatedHash is not None:
            repeatedHash.value = value
            return
        
        newHash = Hash(key, value)
        newHash.next = self.table[listKey]
        self.table[listKey] = newHash

    def search(self, key):
        listKey = self._hash(key)

        current = self.table[listKey]
        while current is not None:
            if current.key == key : return current
            current = current.next
        return None
    
    def countByCapacity(self):
        listaSum = [0 for _ in range(self.M)] 
        for i,v in enumerate(self.table):
            aux = v
            while aux is not None:
                listaSum[i] += 1
                aux = aux.next
        return listaSum
                





if __name__ == "__main__":
    print(hash("pinto"))
    tabela = tabelaHash(5)
    tabela.put("p","g")
    #print(tabela.search("p").value)
    tabela.put("p","g1")
    #print(tabela.search("p").value)
    for i in tabela.table:
        if i == None:continue
        print(i.key)
    print(tabela)


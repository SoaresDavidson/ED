class Node():
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None

    def getElem(self):
        return self.elem
    
    def __str__(self):
        return str(self.elem)
    
    def setElem(self, elem):
        self.elem = elem
    
class DoubleList():
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.count = 0

    def push_back(self, elem): #* Adiciona o elemento ao final da lista
        if self.tail.elem == None:
            self.tail.elem = elem
            self.tail.prev = self.head
            self.tail.next = None
        else:
            n = Node(elem)
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        self.count += 1

    def push_front(self, elem): #*Adiciona o elemento ao começo da lista
        if self.head.elem == None:
            self.head.elem = elem
            self.head.prev = None
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            n = Node(elem)
            self.head.prev = n
            if self.head.next is self.tail and self.tail.elem is None:
                self.tail = self.head
                self.tail.next = None
            n.next = self.head
            n.prev = None
            self.head = n
        self.count += 1
    
    def getTail(self):
        return self.tail
    
    def getHead(self):
        return self.head
    
    def insert(self, elem): #* Função de inserção ordenada em ordem crescente
        if self.head.elem == None or elem < self.head.elem:
            self.push_front(elem)
        elif self.tail.elem == None or elem > self.tail.elem:
            self.push_back(elem)
        else: #* Insere o elemento em seu devido lugar, respeitando a ordem crescente
            n = self.head
            while n is not None:
                if n.elem > elem:
                    break
                n = n.next
            new = Node(elem)
            n.prev.next = new
            n.prev = new
            new.prev = n.prev
            new.next = n

    def isThere(self, elem):   #* Verifica se um elemento está na lista
        n = self.head
        while n != None:
            if n.elem == elem:
                return True
            n = n.next
        return False
    
    def exclude(self, elem):
        if self.isThere(elem): #*Checa se o elemento a ser excluído existe
            self.count -= 1
            n = self.head
            while n.elem is not None:
                if n.elem == elem:
                    break
                n = n.next
            if n == self.head: #*Caso o elemento seja o head, a gente precisa alterá-lo diretamente
                self.head = n.next
            elif n == self.tail: #*O mesmo serve para a tail
                self.tail = n.prev
            previous = n.prev
            next = n.next
            #*Nódulos nulos não podem ter ponteiros não nulos
            if previous is not None:
                previous.next = next
            if next is not None:
                next.prev = previous
            return True
        else:
            return False
    
    def getCount(self):
        return int(self.count)
    
    def getElements(self): #* Retorna uma lista com os elementos da lista duplamente encadeada
        elements = []
        n = self.head
        while n != None:
            if n.elem != None:
                elements.append(str(n))
            n = n.next
        return elements
            

print("Bem vindo ao simulador de lista encadeada dupla. Segue menu de opções")
lista = DoubleList()
while True:
    print("1 - Adicionar elementos\n2 - Verificar se elemento está na lista\n3 - Excluir elemento\n4 - Exibir todos os elementos e quantidade\nOutro - Fechar o programa")
    x = input()
    try:
        x = int(x)
    except:
        print("Programa será fechado")
        exit()
    if x == 1:
        temp = int(input("Digite o elemento a ser adicionado: "))
        lista.insert(temp)
        print("Feito!")
    elif x == 2:
        temp = int(input("Digite o elemento a ser procurado: "))
        if lista.isThere(temp):
            print("Elemento encontrado!")
        else:
            print("Elemento não encontrado")
    elif x == 3:
        temp = int(input("Digite o elemento a ser excluído: "))
        if lista.exclude(temp):
            print(f"Elemento {temp} excluído")
        else:
            print(f"Elemento {temp} não excluído, pois não existe na lista")
    elif int(x) == 4:
        print(f"Lista: {lista.getElements()}. Quantidade: {lista.getCount()}")
    else:
        print("Programa será fechado")
        exit()


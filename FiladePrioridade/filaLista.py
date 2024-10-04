class Pessoa:
    def __init__(self,nome,idade):
        self.next = None
        self.nome = nome
        self.idade = idade

class Priority_Queue:
    def __init__(self):
        self.head = None
        self.back = None
        self.filaComum = 0
        self.filaPrioridade = 0

    def prioridade(self,pessoa):
        if pessoa.idade < 60:
            return 0
        if pessoa.idade < 70:
            return 1
        if pessoa.idade < 80:
            return 2
        if pessoa.idade < 90:
            return 3
        if pessoa.idade < 100:
            return 4
        if pessoa.idade >=100:
            return 5                    

    def push(self,nome,idade):
        pessoa = Pessoa(nome,idade)
        if idade >= 60:
            self.adicionar_prioridade(pessoa)
        else:
            self.adicionar_comum(pessoa)  

    def adicionar_prioridade(self,pessoa):
        nível_prioridade = self.prioridade(pessoa)
        self.filaPrioridade+=1
        if self.head is None:
            self.back = pessoa
            self.head = pessoa
            return 
        atual = self.head
        anterior = None 
        while atual is not None:
            if  nível_prioridade > self.prioridade(atual):
                break
            anterior = atual
            atual = atual.next
        if anterior is None:
            pessoa.next = self.head
            self.head = pessoa   
        else:
            pessoa.next = atual   
            anterior.next = pessoa 
        if pessoa.next is None:
            self.back = pessoa    
            
    def adicionar_comum(self,pessoa):
        self.filaComum+=1
        if self.back is None:
            self.head = pessoa
            self.back = pessoa
        else:
            self.back.next = pessoa
            self.back = pessoa          

    def __repr__(self):
        atual = self.head
        msg = ''
        while atual is not None:
            msg+=f' {atual.nome} {atual.idade}' 
            atual = atual.next   
        return msg


fila = Priority_Queue()
fila.push('ana',50)
fila.push('joao',60)
print(fila)              

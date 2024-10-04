class Pessoa:
    peso = 0
    def __init__(self,nome,idade):
        self.next = None
        self.nome = nome
        self.idade = idade

        

class Priority_Queue:
    def __init__(self):
        self.head = None
        self.back = None
        self.filaComum = 0
        self.atendidasComum = 0
        self.atendidasPrioridade = 0
        self.filaPrioridade = 0

    def prioridade(self,pessoa):
        if pessoa.idade < 70:
            return 1
        if pessoa.idade < 80:
            return 2
        if pessoa.idade < 90:
            return 3
        if pessoa.idade < 100:
            return 4
        return 5                    

    def size_prioridade(self):
        return self.filaPrioridade - self.atendidasPrioridade

    def size_comum(self):
        return self.filaComum - self.atendidasComum    


    def push(self,nome,idade):
        pessoa = Pessoa(nome,idade)
        if idade >= 60:
            self.adicionar_prioridade(pessoa)
        else:
            self.adicionar_comum(pessoa) 
    def empty(self):
        if self.head is not None:
            return False
        return True

    def pop_front(self):
        if not self.empty():
            aux = f'{self.head.nome},{self.head.idade}'
            if self.head.peso != 0: #se a pessoa que esta no começo da fila for preferencial
                self.atendidasPrioridade+=1
            else:
                self.atendidasComum+=1    
            self.head = self.head.next 
            return aux        

    def adicionar_prioridade(self,pessoa):
        pessoa.peso = self.prioridade(pessoa)
        self.filaPrioridade+=1
        if self.head is None:
            self.back = pessoa
            self.head = pessoa
            return 
        atual = self.head
        anterior = None 
        while atual is not None:
            if  pessoa.peso > atual.peso:
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

def color(txt,cor):
    print(f'\033[{cor}{txt}\033[m')

def menu():
    #alguem cria o menu e utiliza a função de cima ela modifica as cores no terminal
    #se tiver duvida na internet tem os codigos das cores ou eu posso ensinar como fazer
    pass    


#teste
fila = Priority_Queue()
fila.push('ana',71)
fila.push('joao',60)
fila.push('pedro',50)
fila.push('raquel',80)
fila.push('maria',61)
fila.push('saleh',19)
fila.push('marcelo',63)
fila.push('victor',62)
fila.pop_front()
fila.pop_front()
print(fila.size_prioridade())
print(fila.size_comum())
print(fila)  

#a parte principal vai ser aqui mas vou deixar comentado
'''
if __name__ == '__main__':
    while True:
        menu()
'''
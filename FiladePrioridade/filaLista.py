import os, menu_module
class Pessoa:
    #peso = nivel de prioridade
    peso = 0
    def __init__(self,nome,idade):
        self.next = None
        self.nome = nome
        self.idade = int(idade)

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
        if pessoa.idade >= 60:
            self.adicionar_prioridade(pessoa)
        else:
            self.adicionar_comum(pessoa) 

    def empty(self):
        return self.head is None
        #if self.head is not None:
        #    return False
        #return True

    def pop_front(self):
        if not self.empty():
            aux = f'{self.head.nome}: {self.head.idade}'
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

        while atual is not None and pessoa.peso <= atual.peso:
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
            msg+=f'{atual.nome}: {atual.idade} anos, ' 
            atual = atual.next 
        if msg:
            msg = msg[:-2]
        return msg

def color(txt,cor):
        print(f'\033[{cor}m{txt}\033[m')

#teste


#a parte principal vai ser aqui mas vou deixar comentado

if __name__ == '__main__':
    menu = menu_module.Menu()
    fila = Priority_Queue()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if menu(fila):
            break
        
    color('Atendimento encerrado','032;1')
    color('Estátisticas: ','032;1')
    color(f'Atendimentos: {fila.atendidasComum+fila.atendidasPrioridade}','034;1')
    color(f'Percentual fila prioritária: {(fila.filaPrioridade/(fila.filaComum+fila.filaPrioridade))*100:.2f}%','034;1')
    color(f'Percentual fila comum: {(fila.filaComum/(fila.filaComum+fila.filaPrioridade))*100:.2f}%','034;1')
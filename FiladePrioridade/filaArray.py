import itertools, os, menu_module

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getIdade(self):
        return self.idade

    def getNome(self):
        return self.nome
    
    def __str__(self):
        return str(self.nome) + '(' + str(self.idade) + ')'
    
class Array():
    def __init__(self, lim):
        self.elem = [None for i in range(lim)]
        self.head = 0
        self.tail = 0
        self.lim = lim
        self.attended = 0

    def getId(self, id):
        return self.elem[id]
    
    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail
    
    def getAttended(self):
        return self.attended
    
    def hasReachedLim(self, describer):
        return describer == self.lim

    def filled(self):
        i = 0
        for _ in range(self.lim):
            if self.elem[_] is not None: i += 1
        return i
    
    def isFull(self):
        return self.filled() == self.lim
    
    def empty(self):
        return self.filled() == 0
    
    def push(self, nome, idade):
        elem = Pessoa(nome,idade)
        if self.isFull(): return False
        
        self.elem[self.tail] = elem
        self.tail += 1

        if self.hasReachedLim(self.tail): self.tail = 0
        return True
    
    def pop_front(self):
        if self.empty(): return

        aux = self.elem[self.head]

        self.elem[self.head] = None
        self.head += 1

        if self.hasReachedLim(self.head): self.head = 0

        self.attended += 1
        return aux
        

    def __str__(self):
        res = ""
        i = self.head
        while i != self.tail:
            if i == self.lim: 
                i = 0
            res += str(self.elem[i]) + ", "
            i += 1
        if i != self.head:
            res += '\n'
        return res
    
class PriorityQueue():
    def __init__(self,cente:Array, nona:Array, octa:Array, septa:Array, sexa:Array, comuns:Array):
        self.prioridades = [cente, nona, octa, septa, sexa]
        self.comuns = comuns

    def empty(self):
        for i in self.prioridades: 
            if not i.empty(): 
                return False

        if not self.comuns.empty(): return False

        return True
            
    def push(self, nome, idade):
        if idade >= 100:
            self.prioridades[0].push(nome,idade)
        elif idade >= 90:
            self.prioridades[1].push(nome,idade)
        elif idade >= 80:
            self.prioridades[2].push(nome,idade)
        elif idade >= 70:
            self.prioridades[3].push(nome,idade)
        elif idade >= 60:
            self.prioridades[4].push(nome, idade)
        else:
            self.comuns.push(nome, idade)
        
    def pop_front(self):
        #o menu checa se a fila está vazia ou essa checagem adcional é so para achar
        #qual fila tem pessoa, mas é garantido que esse metodo so executa quando a fila tem gente
        for filaPrioridade in self.prioridades:
            if not filaPrioridade.empty(): 
                return filaPrioridade.pop_front()
            
        if not self.comuns.empty(): 
            return self.comuns.pop_front()

        return False
    
    def __str__(self):
        res = ""
        for i in self.prioridades:
            res += str(i)
        res += str(self.comuns)
        return res

print("Bem-vindo à fila de prioridade com array")    


x = int(input("Qual o tamanho das filas a serem feitas? "))
comuns = Array(x)
sexa = Array(x)
septa = Array(x)
octa = Array(x)
nona = Array(x)
cente = Array(x)

lista = ['C', 'P', 'P']
ciclo = itertools.cycle(lista)

fila = PriorityQueue(cente, nona, octa, septa, sexa, comuns)
menu = menu_module.Menu(True)

while True:
    if menu.executar(fila): break

#try: 
 #   atendidos_prioridade = sum(fila.getAttended() for fila in prioridades)
  #  atendidos_comum = comuns.getAttended()
#
 #   if atendidos_comum + atendidos_prioridade > 0:
  #      print(f"Relação Atendimentos Prioridade/Total: {(atendidos_prioridade / (atendidos_prioridade + atendidos_comum) * 100):.2f}%")
   # else:
   #     print("Nenhum atendimento realizado")
#except Exception as e:
#    print(f"Erro: {e}")
#    print("Filas vazias. Programa encerrando.")
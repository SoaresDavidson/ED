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
    
    def filled(self):
        i = 0
        for _ in range(self.lim):
            if self.elem[_] is not None: i += 1
        return i
    
    def isFull(self):
        return self.filled() == self.lim
    
    def isEmpty(self):
        return self.filled() == 0
    
    def add(self, elem: 'Pessoa'):
        if not self.isFull():
            if self.tail == self.lim:
                self.tail = 0
                self.elem[0] = elem
            else:
                self.elem[self.tail] = elem
                self.tail += 1
            return True
        return False
    
    def attend(self):
        if not self.isEmpty():
            if self.head == self.lim:
                self.elem[self.lim - 1] = None
                self.head = 0
            else:
                self.elem[self.head] = None
                self.head += 1
            self.attended += 1
            return True
        return False
    
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


print("Bem-vindo à fila de prioridade com array")    
x = int(input("Qual o tamanho das filas a serem feitas? "))
comuns = Array(x)
sexa = Array(x)
septa = Array(x)
octa = Array(x)
nona = Array(x)
cente = Array(x)
prioridades = [cente, nona, octa, septa, sexa]
lista = ['C', 'P', 'P']
ciclo = itertools.cycle(lista)

# Passando prioridades e fila comum separadamente
while True:
    menu = menu_module.Menu_Array()
    if menu.executar(prioridades + [comuns]):  # Unindo prioridades e comuns
        break

try:
    # Calculando os atendimentos prioritários corretamente
    atendidos_prioridade = sum(fila.getAttended() for fila in prioridades)
    atendidos_comum = comuns.getAttended()

    if atendidos_comum + atendidos_prioridade > 0:
        print(f"Relação Atendimentos Prioridade/Total: {(atendidos_prioridade / (atendidos_prioridade + atendidos_comum) * 100):.2f}%")
    else:
        print("Nenhum atendimento realizado")
except Exception as e:
    print(f"Erro: {e}")
    print("Filas vazias. Programa encerrando.")



class Node:
    def __init__(self, i_data):
        self.next = None
        self.data = i_data

    def getData(self):
        return self.data

    def setData(self, n_data):
        self.data = n_data 

class List:
    def __init__(self):
        self.head = None
        

    def empty(self):
        return self.head is None

    def size(self):
        aux = self.head
        sz = 0
        while aux is not None:
            sz+=1
            aux = aux.next
        return sz 

    def find_tail(self):
        current_node = self.head
        while current_node is not None:
            if current_node.next is None:
                return current_node
            current_node = current_node.next      
        return None             


    def search(self,value):
        value = str(value).upper()
        aux = self.head
        while aux is not None:
            if str(aux.getData()).upper() == value:
                return True
            aux = aux.next 
        return False    

    def push_back(self, value):
        if self.search(value) is False:
            tail = self.find_tail()
            node = Node(value)
            if self.empty(): 
                self.head = node
            else:
                tail.next = node 
                tail = node    
        else:
            print('item ja cadastrado')        

    def erase(self, value):
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if str(current_node.getData()).upper() == str(value).upper():
                if previous_node is None:
                    self.head = current_node.next
                    return
                else:     
                    previous_node.next = current_node.next
                    return
                
                current_node = current_node.next  
            else:
                previous_node = current_node  
                current_node = current_node.next        
                

    def push_front(self, value):
        if self.search(value) is False:
            novo = Node(value)
            novo.next = self.head
            self.head = novo
        else:
            print('item ja cadastrado ')        

    def __repr__(self):
        aux = self.head
        msg = ''
        while aux is not None:
            msg += str(aux.getData()) + ' '
            aux = aux.next
        return msg.strip() 


def menu():
    l = List()
    while True:
        print("\nMenu:")
        print("1. Inserir elemento no início da lista")
        print("2. Inserir elemento no final da lista")
        print("3. Verificar se um elemento existe na lista")
        print("4. Excluir um elemento da lista")
        print("5. Mostrar todos os elementos e a quantidade")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = input("Digite o elemento: ")
            l.push_front(valor)
        elif opcao == "2":
            valor = input("Digite o elemento: ")
            l.push_back(valor)
        elif opcao == "3":
            valor = input("Digite o elemento: ")
            existe = l.search(valor)
            print("Elemento encontrado!" if existe else "Elemento não encontrado.")
        elif opcao == "4":
            valor = input("Digite o elemento: ")
            l.erase(valor)
        elif opcao == "5":
            print(f'[{l}]')
            print(f"Tamanho da lista: {l.size()}")
        elif opcao == "6":
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()

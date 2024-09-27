class Node:
    def __init__(self, i_data):
        self.next = None
        self.data = str(i_data)

    def getData(self):
        return self.data

    def setData(self, n_data):
        self.data = str(n_data) 

class List:
    def __init__(self):
        self.head = None
        self.back = None

    def empty(self):
        return self.head is None

    def size(self):
        sum = 0
        aux = self.head
        while aux is not None:
            sum+=1
            aux = aux.next
        return sum     

    def search(self,value):
        value = str(value).upper()
        aux = self.head
        while aux is not None:
            if aux.getData().upper() == value:
                return True
            aux = aux.next 
        return False    

    def push_back(self, value):
        if self.search(value) is True:
            print('item ja cadastrado')
            return
    
        node = Node(value)
        if self.empty(): 
            self.head = node
            self.back = node
        else:
            self.back.next = node 
            self.back = node 
                   

    def erase(self,value):
        current_node = self.head
        previus_node = None
        while current_node is not None:
            if current_node.getData() == str(value):
                if previus_node is None:
                    self.head = current_node.next
                    if self.empty():
                        self.back = None
                        return
                else:
                   previus_node.next = current_node.next 
                if current_node is self.back:
                    self.back = previus_node 

                current_node = current_node.next      

            else:            
                previus_node = current_node    
                current_node = current_node.next  
             
                


    def push_front(self, value):
        if self.search(value) is False:
            novo = Node(value)
            novo.next = self.head
            self.head = novo
            if self.back is None:  
                self.back = novo
        else:
            print('item ja cadastrado ')        

    def __repr__(self):
        aux = self.head
        msg = ''
        while aux is not None:
            msg += str(aux.getData()) + ' '
            aux = aux.next
        return msg.strip() 


if __name__ == "__main__":
    l = List() 
    l.push_front(1)
    l.push_back("raimundo")
    l.push_front("Raimundo")
    l.push_back(1)
    l.push_back(2)
    l.push_back(3)
    l.push_front(4)
    l.search(1)
    print(l.size())
    l.erase(1)

    print(l)
    print(l.size())
    print(l)
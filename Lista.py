

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


if __name__ == "__main__":
    l = List() 
    for i in range(51):
        l.push_back(i)
    for i in range(-1,-51,-1):
        l.push_front(i)
    print(l)
    print(l.size())
    for i in range(51):
        l.erase(i)
    print(l)
    print(l.size())
    print(l)

    l1 = List()
    l1.push_back("ana")
    l1.push_back("ANA")
    l1.push_back("Ana")
    l1.push_back("beatriz")
    l1.push_front("carlos")
    print(l1) 
   
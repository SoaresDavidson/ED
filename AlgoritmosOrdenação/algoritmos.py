import unidecode
import time

def tictoc(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time() - t1
        print(f"{func.__name__} levou {t2} segundos")
        return result
    return wrapper


def heapify(arr:list, n:int, i:int) -> None:
    largest = i 
    
    l = 2 * i + 1 
    
    r = 2 * i + 2  

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        heapify(arr, n, largest)

@tictoc
def heapSort(arr:list) -> None:
    size = len(arr) 

    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, size, i)

    for i in range(size - 1, 0, -1):

        arr[0], arr[i] = arr[i], arr[0] 

        heapify(arr, i, 0)
        
@tictoc
def insertionSort(arr: list) -> None:
    for i,value in enumerate(arr):  
        j = i-1
        while j >= 0 and value < arr[j]: 
            arr[j+1] = arr[j]  
            j -= 1
        arr[j+1] = value

@tictoc
def merge_sort(array:list, left:int, right:int) -> None:
    if left < right:
        mid = (left + right) // 2  
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)

        merge(array, left, mid, right)

def merge(array:list, left:int, mid:int, right:int) -> None: 
    left_half = array[left:mid + 1]
    right_half = array[mid + 1:right + 1]
    i = 0  
    j = 0 
    k = left  
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i] 
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1   
    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1

@tictoc
def bubble_sort(array) -> None:      
    troca = False
    while True:
        troca = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                troca = True
                aux = array[i+1]
                array[i+1] = array[i]
                array[i] = aux
        if troca is False:
            break

def quick_sort(array, ini, fim) -> list:
    if ini >= fim:
        return array
    pivo = array[ini]
    i, j = ini + 1, fim

    while True:
        while i <= j and unidecode.unidecode(array[i].lower()) <= unidecode.unidecode(pivo.lower()):
            i += 1
        while i <= j and unidecode.unidecode(array[j].lower()) >= unidecode.unidecode(pivo.lower()):
            j -= 1
        if i > j:
            break
        array[i], array[j] = array[j], array[i]

    array[ini], array[j] = array[j], array[ini]

    quick_sort(array, ini, j - 1)  
    quick_sort(array, j + 1, fim)  
    return array

@tictoc
def quick(array:list) -> list:
    from random import shuffle
    shuffle(array)  
    return quick_sort(array, 0, len(array) - 1)  


if __name__ == "__main__":
    arr = ["s","o","r","t","e","x","a","m","p","l","e"]
    
    insertionSort(arr)
    #heapSort(arr)
    #quick(arr)
    #merge_sort(arr, 0, len(arr)-1)
    #print(arr)
    #print(*arr)
def heapify(arr, n, i):
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

def heapSort(arr):
    size = len(arr) 

    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, size, i)

    for i in range(size - 1, 0, -1):

        arr[0], arr[i] = arr[i], arr[0] 

        heapify(arr, i, 0)

def insertionSort(arr):
    for i,value in enumerate(arr):  
        j = i-1
        while j >= 0 and value < arr[j]: 
            arr[j+1] = arr[j]  
            j -= 1
        arr[j+1] = value

if __name__ == "__main__":
    arr = ["s","o","r","t","e","x","a","m","p","l","e"]
    #insertionSort(arr)
    heapSort(arr)
    print(arr)

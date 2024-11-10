import time

def tictoc(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time() - t1
        #print(f"{func.__name__} levou {t2} segundos")
        return t2
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
def shellSort(nums):
    n = len(nums)
    h = int (n//2)
    while h > 0:
            for i in range(h, n):
                c = nums[i]
                j = i
                while j >= h and c < nums[j - h]:
                    nums[j] = nums[j - h]
                    j = j - h
                    nums[j] = c
            h = h // 2
    return nums

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
def merge_sort(array:list, left:int = 0, right:int = None) -> None:
    if right == None: right = len(array) - 1

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
def bubbleSort(arr:list):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

def partition(arr:list, low:int, high:int):
    
    # Choose the pivot
    pivot = arr[high]
    
    # Index of smaller element and indicates 
    # the right position of pivot found so far
    i = low - 1
    
    # Traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    # Move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    return i + 1

# Swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# The QuickSort function implementation
@tictoc
def quickSort(arr:list, low:int = 0, high:int = None) -> None:
    if high == None:high = len(arr) - 1
    if low < high:
        
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        
        # Recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
@tictoc
def selectionSort(array):
    size = len(array)
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])


if __name__ == "__main__":
    arr = ["s","o","r","t","e","x","a","m","p","l","e"]
    
    #insertionSort(arr)
    #heapSort(arr)
    #quick(arr)
    merge_sort(arr, 0, len(arr)-1)
    #print(arr)
    #print(*arr)

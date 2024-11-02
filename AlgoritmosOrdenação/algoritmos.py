def insertionSort(arr):
    for i,value in enumerate(arr):  
        j = i-1
        while j >= 0 and value < arr[j]: 
            arr[j+1] = arr[j]  
            j -= 1
        arr[j+1] = value 
  
if __name__ == "__main__":
    arr = ["s","o","r","t","e","x","a","m","p","l","e"]
    insertionSort(arr)
    print(arr)

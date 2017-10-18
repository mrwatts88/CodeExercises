from builtins import range
import random

def bubbleSort(arr):    
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

myArray = []
for i in range(20):
    myArray.append(random.randint(0,100))

bubbleSort(myArray)

print(myArray)
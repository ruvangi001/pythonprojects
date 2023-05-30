import numpy as np

def binarysearch(arr,element,start,end):
    while start<=end:
        mid=int((start+end)/2)

        if arr[mid]==element:
            return mid

        elif arr[mid] < element:
            start=mid+1

        else:
            end=mid-1
    return -1

ar = [5,7,13,9,32,42,33,54,56,88]
arr = np.sort(ar)

start=0;end=len(arr)-1
element = int(input('Enter the element you want to search for:- '))

result = binarysearch(arr,element,start,end)

if result != -1:
    print('Element found at index ',result)
else:
    print('Element not found.')
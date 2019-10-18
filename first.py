import time
from datetime import datetime



file = open("ai183.txt", "r")
arr = []

fTest = False
sTest = False

while True:
    check = file.read(1)
    if not check:
        break

    if check == "1":
        check = file.read(1)
        if check == "4":
            fTest = True
            check = file.read(1)
            if check == ":":
                sTest = True

    if fTest == True and sTest == True:
        file.seek(file.tell() + 1)
        check = file.read(1)
        while check != "}":
            arr.append(int(check))
            check = file.read(1)
        break

file.close()
print("array: ", arr)


def mergeSort(arr):
    if len(arr) < 2: return arr

    result, mid = [], int(len(arr) / 2)

    right = mergeSort(arr[mid:])
    left = mergeSort(arr[:mid])

    while (len(left) > 0) and (len(right) > 0):
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    result.extend(left + right)
    return result



def heapSort(arr):
    length = len(arr)

    for i in range(length, -1, -1):
        heap(arr, length, i)

    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)
    return arr

def heap(arr, length, i):
    largest = i
    L = 2 * i + 1
    R = 2 * i + 2

    if L < length and arr[i] < arr[L]:
        largest = L

    if R < length and arr[largest] < arr[R]:
        largest = R

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr, length, largest)


def quickSort(arr):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        first = arr[0]
        for number in arr:
            if number < first:
                less.append(number)
            elif number == first:
                equal.append(number)
            elif number > first:
                greater.append(number)
        return quickSort(less) + equal + quickSort(greater)
    else:
        return arr



start_time = datetime.now()
print("merge sort: ", mergeSort(arr))
end_time = datetime.now()
print('time: {}'.format(end_time - start_time))#time: 0:00:00.015381


start_time = datetime.now()
print("heap sort: ", heapSort(arr))
end_time = datetime.now()
print('time: {}'.format(end_time - start_time))#time: 0:00:00.013996


start_time = datetime.now()
print("quick sort: ", quickSort(arr))
end_time = datetime.now()
print('time {}'.format(end_time - start_time)) #time 0:00:00.012205

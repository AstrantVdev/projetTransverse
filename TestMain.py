from random import *

def quickSort(list, left=0, right=len(list) -1):
    if left >= right:
        return

def partition(list, left, right):
    pivotValue=list[right]
    partitionIndex=left
    for i in range(left, right, 1):
        if list[i] < pivotValue:
            swap(list, i, partitionIndex)
            partitionIndex+=1

    swap(list, right, partitionIndex)


def swap(list, firstIndex, secondIndex):
    temp=list[firstIndex]
    list[firstIndex]=list[secondIndex]
    list[secondIndex]=temp





#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def min_heap(arr,i):
    l = 2*i + 1
    r = 2*i + 2
    smallest = i
    size = len(arr)
    
    if l < size and arr[l] < arr[i]:
        smallest = l
    if r < size and arr[r] < arr[smallest]:
        r = smallest
    if smallest != i:
        small = arr[smallest]
        bigger = arr[i]
        arr[i] = small
        arr[smallest] = bigger
        min_heap(arr,smallest)
    return arr

def heapify(arr):
    end_leaf = math.floor(len(arr)/2) - 1
    for i in range(end_leaf,-1,-1):
        arr = min_heap(arr,i)
    return arr

def magic(arr):
    bland_cookie = arr[0]
    leaf = arr.pop()
    arr[0]  = leaf
    arr = min_heap(arr,0)
    arr[0] = 2*arr[0] + bland_cookie
    arr = min_heap(arr,0)
    return arr
      
def cookies(k, A):
    counter = 0
    if len(A) < 1:
        return -1
    cookie_tray = heapify(A)
    while cookie_tray[0] < k:
        counter += 1
        cookie_tray = magic(cookie_tray)
    return counter
    

  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()

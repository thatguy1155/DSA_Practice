import math
#array we have
bad_arr = [3,6,5,0,8,2,1,9]
good_arr = [0,3,1,6,8,2,5,9]

class Min_Heap():
  def __init__(self):
    self.arr_to_check = []

  def heapify(self,arr,index):
    l = 2 * index + 1
    r = 2 * index + 2
    heap_size = len(arr)

    if l < heap_size and arr[l] < arr[index]:
      smallest = l
    else:
      smallest = index
    if r < heap_size and arr[r] < arr[smallest]:
      smallest = r

    if smallest != index:
      node_index = arr[index]
      node_largest = arr[smallest]
      arr[index] = node_largest
      arr[smallest] = node_index
      arr = self.heapify(arr,smallest)
    return arr
  def meta_heap(self,arr):
    leaf_point = int((math.floor(len(arr)/2))-1)
    for i in range(leaf_point,-1,-1):
      arr = self.heapify(arr,i)
    return arr


    
  
  def print_arr(self):
    print(str(self.arr_to_check))
heap = Min_Heap()
print(str(heap.meta_heap(bad_arr)))
#heap.print_arr()


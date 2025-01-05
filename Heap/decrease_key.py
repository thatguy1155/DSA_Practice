import math
#array we have
orig_arr = [9,8,7,6,5,4,3,2,1]
after_arr = [9,6,7,2,5,4,3,0,1]

class Max_Heap():
  def __init__(self):
    self.arr = []

  def heapify(self,arr,index):
    l = 2 * index + 1
    r = 2 * index + 2
    heap_size = len(arr)

    if l < heap_size and arr[l] > arr[index]:
      largest = l
    else:
      largest = index
    if r < heap_size and arr[r] > arr[largest]:
      largest = r

    if largest != index:
      node_index = arr[index]
      node_largest = arr[largest]
      arr[index] = node_largest
      arr[largest] = node_index
      arr = self.heapify(arr,largest)
    return arr
  
  def meta_heap(self,arr):
    leaf_point = int((math.floor(len(arr)/2))-1)
    for i in range(leaf_point,-1,-1):
      arr = self.heapify(arr,i)
    self.arr = arr
    return arr
  
  def decrease_key(self,i,key):
    arr = self.arr
    if key > arr[i]:
      return arr
    arr[i] = key
    arr = self.heapify(arr,i)
    return arr




    
  
  def print_arr(self):
    print(str(self.arr_to_check))
heap = Max_Heap()
print(str(heap.meta_heap(orig_arr)))
print(str(heap.decrease_key(1,0)))
#heap.print_arr()
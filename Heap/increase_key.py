import math
#array we have
orig_arr = [9,8,7,6,5,4,3]
after_arr = [50,9,7,6,8,4,3]

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
  
  def increase_key(self,i,key):
    arr = self.arr
    if key < arr[i]:
      return arr
    arr[i] = key
    parent_index = (i - 1) // 2
    while i > 0 and arr[i] > arr[parent_index]:
        # Swap current node with parent
        arr[i], arr[parent_index] = arr[parent_index], arr[i]
        # Update index to parent's position
        i = parent_index
        parent_index = (i - 1) // 2
    return arr




    
  
  def print_arr(self):
    print(str(self.arr_to_check))
heap = Max_Heap()
print(str(heap.meta_heap(orig_arr)))
print(str(heap.increase_key(4,50)))
#heap.print_arr()
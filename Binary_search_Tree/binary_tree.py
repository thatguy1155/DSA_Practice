#first create the class of a node

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
   # Compare the new value with the parent node
      if self.data:
         #if less than than current node, if left empty append else recursively analyze lower level
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
          #if greater than current node, do the same in the right direction
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         #if there is no tree then do initial insert
         self.data = data   
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()

#then create the root. here it is 10
# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
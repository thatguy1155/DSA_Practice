#first create the class of a node

class Node:
  def __init__(self,data):
    self.data = data
    self.left = ""
    self.right = ""

  def insert(self,data):
    if data:
      if data > self.data:
        if self.left:
          self.left.insert(data)
        else:
          self.left = Node(data)
      elif data < self.data:
        if self.right:
          self.right.insert(data)
        else:
          self.right = Node(data)
  def print_tree(self):
    if self.left:
      self.left.print_tree()
    print(self.data)
    if self.right:
      self.right.print_tree()
root = Node(10)
root.insert(5)
root.insert(12)
root.print_tree()



# Using Queue
from collections import deque

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def levelOrder(root):
    if root is None:
        return []

    # Create an empty queue for level order traversal
    q = deque()
    res = []

    # Enqueue Root
    q.append(root)
    currLevel = 0

    while q:
        len_q = len(q)
        res.append([])

        for _ in range(len_q):
            # Add front of queue and remove it from queue
            node = q.popleft()
            res[currLevel].append(node.data)

            if node.left is not None or node.right is not None:
              # Enqueue left child
              if node.left is not None:
                q.append(node.left)
              else:
                void  = Node(-1)
                q.append(void)

              # Enqueue right child
              if node.right is not None:
                q.append(node.right)
              else:
                void  = Node(-1)
                q.append(void)
            elif node.data != -999:
               q.append(Node(-999))
               q.append(Node(-999))
               
            
            
        currLevel += 1

    return res
      
if __name__ == "__main__":
    # Create binary tree
    root = Node(2)
    root.left = Node(3)
    root.right = Node(3)
    root.right.right = Node(4)
    root.right.left = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)
    root.right.right.right = Node(8)
    root.right.right.left = Node(9)

    # Perform level order traversal
    res = levelOrder(root)

    # Print the result
    for level in res:
        print(str(level))
        #for data in level:
            #print(data, end=" ")
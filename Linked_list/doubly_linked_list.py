class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Function to traverse the doubly linked list 
# in forward direction
def forward_traversal(head):
  
    # Start traversal from the head of the list
    curr = head
    
    # Continue until the current node is 
    # null (end of the list)
    while curr is not None:
      
        # Output data of the current node
        print(curr.data, end=" ")
        
        # Move to the next node
        curr = curr.next
        
    # Print newline after traversal
    print()

# Function to traverse the doubly linked 
# list in backward direction
def backward_traversal(tail):
  
    # Start traversal from the tail of the list
    curr = tail
    
    # Continue until the current node 
    # is null (end of the list)
    while curr is not None:
      
        # Output data of the current node
        print(curr.data, end=" ")
        
        # Move to the previous node
        curr = curr.prev
        
    # Print newline after traversal
    print()

# Sample usage of the doubly linked list 
# and traversal functions
if __name__ == "__main__":
  
    # Create a doubly linked list with 3 nodes
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    print("Forward Traversal:")
    forward_traversal(head)

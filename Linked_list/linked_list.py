class Node:
    class Node:
      def __init__(self, data):
          self.data = data
          self.next = None

      def insert_at_beginning(head, data):
        new_node = Node(data)
        new_node.next = head
        return new_node
          
      def traverse(head):
        current = head
        while current:
          # Print the current node's data followed by an arrow and space
          print(str(current.data) + " -> ", end=" ")
          current = current.next
        # At the end of the list, print None to indicate no further nodes
      print("None")
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
      
      def delete_head(head):
  
        # Base case if linked list is empty
        if head is None:
            return None

        # Change the head pointer to the next node
        # and free the original head
        temp = head
        head = head.next

        # Free the original head
        del temp

        # Return the new head
        return head
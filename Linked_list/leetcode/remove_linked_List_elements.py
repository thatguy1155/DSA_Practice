class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.val == val:
            while head.val == val:
                if head.next:
                    temp = head
                    head = head.next
                    del temp
                else:
                    return None
            
        if head.next == None:
            if head.val == val:
                return None
            else:
                return head
        pointer = head
        while pointer.next is not None:
            if pointer.next.val == val:
                while pointer.next.val == val:
                    if pointer.next.next is not None:
                        temp = pointer.next.next
                        pointer.next = None
                        pointer.next = temp
                    else:
                        pointer.next = None
                        if pointer.val == val:
                            return None
                        return head    
            pointer = pointer.next
        return head
    
    #for better solution create a dummy head and do the one operation from before zero
  
    class BestSolution:
      def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
          dummy = ListNode(-1)
          dummy.next = head
          current = dummy
          
          while current.next:
              if current.next.val == val:
                  current.next = current.next.next  # Remove node
              else:
                  current = current.next  # Move to next node
          
          return dummy.next
class Solution:
    def delete_head(self,head):
        if head is None:
            return []
        temp = head
        head = head.next
        del temp
        return head
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        stack = []
        while head.next:
            stack.append(head.val)
            head = self.delete_head(head)
        pointer = head
        while len(stack) > 0:
            pointer.next = ListNode(stack.pop(),None)
            pointer = pointer.next
        return head


'''this is an example of in-place reversal'''
class BestSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        res = head #set up the reversed linked list
        ptr = res.next #point to current node being processed in the original list. set to current node
        res.next = None # delete the rest of the original list
        
        while ptr:
            nxt = ptr.next # save next node
            ptr.next = res # replace the next node with the reversed linked list
            res = ptr  
            ptr = nxt

        return res
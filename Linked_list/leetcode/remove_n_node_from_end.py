# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        curr = head
        counter = 1
        while curr.next:
            curr = curr.next
            counter += 1
        target = counter - n
        if target == 0:
            return head.next
        curr = head
        counter = 1
        while curr.next:
            if counter == target:
                curr.next = curr.next.next
                return head
            else:
                curr = curr.next
                counter += 1
        return head

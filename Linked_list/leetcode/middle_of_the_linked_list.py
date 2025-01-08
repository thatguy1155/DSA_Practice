# O(N) complexity

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 2
        pointer1 = head
        pointer2 = head
        while pointer1:
            if counter % 2 != 0:
                pointer2 = pointer2.next
            pointer1 = pointer1.next
            counter +=1
        return pointer2
        
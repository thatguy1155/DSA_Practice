class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return None
        fast = head
        slow = head
        while fast.next is not None:
            if fast.next.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next
            if fast == slow:
                return True
        return False
        
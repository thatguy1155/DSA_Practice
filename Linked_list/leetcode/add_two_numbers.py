# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self,head):
        res = head
        ptr = res.next
        res.next = None

        while ptr:
            nxt = ptr.next
            ptr.next = res
            res = ptr
            ptr = nxt
        return res

    def traverse(self,head):
        num_str = ""

        pointer = head
        while pointer is not None:
            num_str += str(pointer.val)
            pointer = pointer.next

        if num_str == "" or num_str == "0":
            return 0
        else:
            return int(num_str)
        



    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        if l1.next:
            revl1 = self.reverse(l1)
        else:
            revl1 = l1
        if l2.next:
            revl2 = self.reverse(l2)
        else:
            revl2 = l2
        
        num1 = self.traverse(revl1)
        num2 = self.traverse(revl2)
        final_num = num1 + num2
        print(final_num)
        if final_num == 0:
            return ListNode(0,None)
        else:
            stack = []
            num_str = str(final_num)
            answer = ""
            ptr = ""
            for i in num_str:
                stack.append(int(i))
            print(str(stack))
            answer = ListNode(stack.pop(),None)
            ptr = answer
            while len(stack) > 0:
                ptr.next = ListNode(stack.pop(),None)
                ptr = ptr.next
            return answer
    def BestSolution(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            '''this solution works by separating the tens place as carry and adding it to the next iteration'''
            head = ListNode()
            current = head 
            carry = 0 
            while (l1 != None or l2 != None or carry != 0): 
                l1_value = l1.val if l1 else 0
                l2_value = l2.val if l2 else 0 
                value = l1_value + l2_value + carry 
                current.next = ListNode(value % 10)
                carry = value // 10 
                l1 = l1.next if l1 else None 
                l2 = l2.next if l2 else None 
                current = current.next 
            return head.next 
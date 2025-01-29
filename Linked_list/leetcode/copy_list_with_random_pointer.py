# my attept

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        list_dict = {}
        current = head
        index = 0
        while current:
            list_dict[(current.val,index)] = Node(current.val,None,None)
            current = current.next
            index += 1
        
        print(str(list_dict))
        current = head
        index = 0
        
        while current:
            if current.next:
                list_dict[(current.val,index)].next = list_dict[(current.next.val,index)]
            if current.random:
                list_dict[(current.val,index)].random = list_dict[(current.random.val,index)]
            current = current.next
            index += 1
        return list_dict[head.val]
#actual solution: key takeaway is you can use a lik=nkedlist node as a key in a hash map
    class Solution:

      def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
          if head == None:
              return None
          list_dict = {}
          current = head
          while current:
              list_dict[current] = Node(current.val,None,None)
              current = current.next
          
          current = head
          
          while current:
              if current.next:
                  list_dict[current].next = list_dict[current.next]
              if current.random:
                  list_dict[current].random = list_dict[current.random]
              current = current.next
          return list_dict[head]
        

    
        

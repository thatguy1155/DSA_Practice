class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        answer = -1
        first_item_list = []
        for i,j in enumerate(haystack):
            if j == needle[0] and i <= (len(haystack) - len(needle)):
                first_item_list.append(i)
        fi_queue = deque(first_item_list)
        while len(fi_queue) > 0:
            index = fi_queue.popleft()
            index_pointer = index
            n_queue = deque(needle)
            while n_queue[0] == haystack[index]:
                n_queue.popleft()
                index += 1
                if len(n_queue) == 0:
                    return index_pointer
        return -1
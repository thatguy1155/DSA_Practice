class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        max_count = 0
        top_boy = -999999999
        curr_num = -999999999

        for i in nums:
            if i != curr_num:
                counter = 1
                curr_num = i
            else:
                counter += 1
            if counter > max_count:
                max_count = counter
                top_boy = curr_num
        return top_boy
            

        
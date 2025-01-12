class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prev_num = -9999999999
        
        pointer = 0
        while pointer < len(nums):
            if nums[pointer] == prev_num:
                del nums[pointer]
            else:
                prev_num = nums[pointer]
                pointer += 1
        
        
        return len(nums)
            
class BestSolution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for i in range(len(nums)):
            if nums[i] > nums[left]:
                left += 1
                nums[left] = nums[i]
        return left + 1
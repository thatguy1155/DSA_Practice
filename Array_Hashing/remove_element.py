class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums == []:
            return 0
        not_val = 0
        for i in range(len(nums)):
            if nums[i] == val:
                while nums[i] == val:
                 del nums[i]
                 if len(nums) == 0:
                    return 0
                 nums.append(-1)
            else:
                not_val += 1
        
        while nums[-1] == -1:
            nums.pop()
            if nums == []:
                return 0
        
        return not_val
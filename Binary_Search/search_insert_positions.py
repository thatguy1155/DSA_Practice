class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        aux = 0
        if len(nums) == 0:
            return 0
        if target <= nums[0]:
            return 0
        elif target > nums[len(nums) - 1]:
            return len(nums)
        i = len(nums)//2
        while nums[i] != target:
            if len(nums) == 2:
                if nums[0] >= target:
                    return aux
                elif nums[1] >= target:
                    return aux + 1
                else:
                    return aux + 2
            if len(nums) == 1:
                if nums[0] >= target:
                    return aux
                else:
                    return aux + 1
            if nums[i] > target:
                nums = nums[:i]
            elif nums[i] < target:
                aux += len(nums[:i])
                nums = nums[i:]
            else:
                return i + aux
            i = len(nums)//2
        return i + aux
            
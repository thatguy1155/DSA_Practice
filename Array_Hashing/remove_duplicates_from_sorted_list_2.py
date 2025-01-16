class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == None:
            return 0
        if len(nums) < 3:
            return len(nums)
        curr_num = -999999
        counter = 0
        i = 0
        while i < len(nums):
            if nums[i] == curr_num:
                counter += 1
                if counter > 2:
                    while nums[i] == curr_num:
                        del nums[i]
                        if len(nums) == i:
                            break
                else:
                    i += 1
            else:
                curr_num = nums[i]
                counter = 1
                i += 1

        return len(nums)
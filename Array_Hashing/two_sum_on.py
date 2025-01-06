class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            rem = target - num
            if num in rem_dict:
                return [rem_dict[num],i]
            if rem not in rem_dict:
                rem_dict[rem] = i
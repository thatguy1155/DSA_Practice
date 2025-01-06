class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        short_list = list(set(nums))
        if len(short_list) != len(nums):
            return True
        else:
            return False
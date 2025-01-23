class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        the_sum = sum(nums[:k])
        max_val = the_sum/k
        for i in range(len(nums) - k):
            the_sum = the_sum - nums[i] + nums[i + k]
            max_val = max(the_sum/k, max_val)
        return max_val

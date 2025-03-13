class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k > len(nums):
            while k > len(nums):
                k = k - len(nums)
        nums2 = nums[-k::] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = nums2[i]
        """
        Do not return anything, modify nums in-place instead.
        """
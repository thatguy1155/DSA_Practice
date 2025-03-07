class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zeroes = [i for i,x in enumerate(nums) if x == 0]
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        if len(zeroes) == 0:
            return True
        else:
            print(str(zeroes))
            void = nums.index(0)
            for zero in zeroes:
                jump = False
                for i in range((zero-1),-1,-1):
                    print(nums[i])
                    print(nums[i] + i)
                    if nums[i] + i >= (len(nums) - 1):
                        return True
                    if nums[i] + i > zero:
                        jump = True
                        break
                if jump == False:
                    return False
            return True
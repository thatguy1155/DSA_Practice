class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {}
        for i,num in enumerate(nums):
            if num not in num_dict:
                num_dict[num] = [i]
            else:
                if abs(num_dict[num][-1] - i) <= k:
                    return True
                else:
                    num_dict[num].append(i)
        return False
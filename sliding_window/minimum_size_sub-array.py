#actual solution:
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0,0
        res = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res



#crappy take 1
def minSubArrayLen(target, nums) -> int:
  if len(nums) == 0:
      return 0
  if max(nums) >= target:
      return 1
  if sum(nums) < target:
      return 0
  if sum(nums) == target:
      return len(nums)
  k = 2
  the_sum = sum(nums[:k])
  while the_sum < target:
      for i in range(len(nums) - k):
          the_sum = the_sum - nums[i] + nums[i + k]
          if the_sum >= target:
              return k
      k += 1
print(minSubArrayLen(15,[1,2,3,4,5]))


#crappy take 2
if len(nums) == 0:
      return 0
  if max(nums) >= target:
      return 1
  if sum(nums) < target:
      return 0
  
  head = 1
  tail = 0
  length = 2
  thee_sum = nums[0] + nums[1]
  while thee_sum < target and head < (len(nums) - 1):
      head += 1
      thee_sum += nums[head]
      length += 1
  
  
  small_len = length
  print(length)
  while tail < (len(nums) + length):
      old_sum = thee_sum
      thee_sum  =  thee_sum - nums[tail] + nums[tail + length]
      if thee_sum > old_sum:
          sub_tail = tail
          sub_length = length
          sub_sum = thee_sum
          while sub_sum > target and sub_length > 0:
              sub_tail += 1
              sub_length -= 1
              sub_sum = sub_sum - nums[sub_tail]
              print(sub_sum)
              print(sub_length)
              print("_________")
              if sub_sum >= target:
                  length = sub_length
                  tail = sub_tail
                  thee_sum = sub_sum
              else:
                  break
      else:
          tail += 1
  return length

#pass 16/21 cases
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) < target:
            if sum(nums) < target:
                return 0
        r = 0
        l = 0
        s = nums[l]
        w = 999999999
        if nums[l] > target:
            return 1

        while r < len(nums):
            if s >= target:
                if len(nums[l:(r+1)]) < w:
                    w = len(nums[l:(r+1)])
                s -= nums[l]
                l += 1
            else:
                s += nums[r]
                r += 1
            print(nums[l:(r+1)])
        while s > target:
            print(nums[l:(r+1)])
            if len(nums[l:(r+1)]) < w:
                w = len(nums[l:(r+1)])
            s -= nums[l]
            l += 1
        return w

        

                
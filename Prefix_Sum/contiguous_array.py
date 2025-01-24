def findMaxLength(nums) -> int:
    num_of_zeros = 0
    num_of_ones = 0
    result = 0
    diff_index = {} #map diff to ending index of the sub_array
    for i, n in enumerate(nums):
        if n == 0:
          num_of_zeroes += 1
        else:
           num_of_ones += 1
        if num_of_zeroes - num_of_ones not in diff_index:
           diff_index[num_of_zeroes - num_of_ones] = i
        if num_of_zeroes == num_of_ones:
           res = num_of_zeroes + num_of_ones
    print(fuck_dict)
    val = fuck_dict[abs(num_of_zeros - num_of_ones)]
    print(val)
    return len(nums) - (val + 1)
    
print(findMaxLength([0,0,1,0,0,0,1,1]))
'''
num of sub arrays in an array of len n is n^2

in the whole array we need to find the longest sub-array ending at a given

the goal is to remove a prefixof the array so that we get an equal number os zeroes and ones
prefix should be as small as possible

use hashmap to map diff to indexes in ones and zeroes. 

'''
'''
def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum_zero = [0] * (len(nums))
        prefix_sum_one = [0] * (len(nums))
        num_of_zeros = 0
        num_of_ones = 0
        for i in range(0,len(nums)):
            if nums[i] == 0:
                num_of_zeros += 1
            else:
                num_of_ones += 1
            prefix_sum_zero[i] = num_of_zeros
            prefix_sum_one[i] = num_of_ones
        print(prefix_sum_zero)
        print(prefix_sum_one)
        if prefix_sum_zero[-1] > prefix_sum_one[-1]:
            return (prefix_sum_one[-1] * 2)
        else:
            return (prefix_sum_zero[-1] * 2)

'''
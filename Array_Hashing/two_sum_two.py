class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]>target:
                right-=1
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                return [left+1,right+1]

class CrappySolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers) - 1
        indexes = []
        

        while len(indexes) == 0:
            if numbers[pointer1] + numbers[pointer2] == target:
                return [pointer1 + 1, pointer2 + 1]
            
            next_int = numbers[pointer1 + 1]
            prev_int = numbers[pointer2 - 1]
            if next_int == numbers[pointer1]:
                if next_int == target/2:
                    return [pointer1 + 1, pointer1 + 2]
                while next_int == numbers[pointer1]:
                    pointer1 += 1
                    next_int = numbers[pointer1 + 1]
            if prev_int == numbers[pointer2]:
                if prev_int == target/2:
                    return[pointer2, pointer2 + 1]
                while prev_int == numbers[pointer2]:
                    pointer2 -= 1
                    prev_int = numbers[pointer2 - 1]
            elif pointer1 == pointer2 - 1:
                pointer1 = 0
                pointer2 -= 1
            else:
                pointer1 += 1
        return indexes

class Solution:
    
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        num_dict = {
            '0':0,
            '1':1,
            '2':4,
            '3':9,
            '4':16,
            '5':25,
            '6':36,
            '7':49,
            '8':64,
            '9':81
        }
        
        magic = False
        while magic == False:
            num_arr = list(str(n))
            if n > 10 and n in num_dict:
                return False
            else:
                num_dict[n] = sum([num_dict[x] for x in num_arr])
                if num_dict[n] == 1:
                    return True
                else:
                    n = num_dict[n]

class BestSolution:
    def isHappy(self, n: int) -> bool:
        seenSum = set()
        dss = n

        while dss not in seenSum:
            seenSum.add(dss)
            dss = self.digitSquaredSum(dss)
            if dss == 1:
                return True            

        return False

    def digitSquaredSum(self, n):
        squaredSum = 0
        q, rem = n//10, n%10
        while q > 0:
            squaredSum += (rem*rem)
            q, rem = q//10, q%10
        squaredSum += (rem*rem)
        return squaredSum
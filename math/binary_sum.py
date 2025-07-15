class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        place_dict = {
            1:0,
        }
        place = 1
        for i in range(0,max_len - 1):
            place = int(str(place) + "0")
            place_dict[place] = 0
        
        a_arr = [int(x) for x in a]
        b_arr = [int(y) for y in b]
        place = 1

        while len(a_arr) > 0 or len(b_arr) > 0:
            if len(a_arr) > 0:
                i = a_arr.pop()
            else:
                i = 0
            if len(b_arr) > 0:
                j = b_arr.pop()
            else:
                j = 0

            if  i + j + place_dict[place] > 1:
                place_dict[place] = (i + j + place_dict[place]) - 2
                if int(str(place) + "0") in place_dict:
                    place_dict[int(str(place) + "0")] += 1
                else:
                    place_dict[int(str(place) + "0")] = 1

            else:
                place_dict[place] = i + j + place_dict[place]
                
            place = int(str(place) + "0")
        final_arr = list(place_dict.keys())
        final_str_arr = []
        while len(final_arr) > 0:
            z = final_arr.pop()
            final_str_arr.append(str(place_dict[z]))
        return ('').join(final_str_arr)
    
#better solution

 class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
    
    #int(a, 2) converts binary to integer
    #bin(int(a, 2) + int(b, 2)) converts their sum into a binary string
    #[2:] removes an unnecessary prefix
        ## 11 -> 1 1
        ##.      1*2^1 + 1*2^0 -> 2+1 -> 3
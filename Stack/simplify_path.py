class Solution:
    def simplifyPath(self, path: str) -> str:
        comp_dict = path.split("/")
        simp_dict = []
        for item in comp_dict:
            if item != '' and item != "." and item != "..":
                simp_dict.append(item)
            elif item == "..":
                if len(simp_dict) > 0:
                    simp_dict.pop()
        answer = "/" + "/".join(simp_dict)
        
        return answer
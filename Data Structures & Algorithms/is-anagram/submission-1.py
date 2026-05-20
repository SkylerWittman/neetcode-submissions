class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                val = s_dict.get(char)
                s_dict[char] += 1
        
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                val = t_dict.get(char)
                t_dict[char] += 1

        for i, char in enumerate(s_dict):
            if t_dict.get(char) != s_dict.get(char):
                return False
            
        return True
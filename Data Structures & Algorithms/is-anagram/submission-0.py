class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t): 
            # return False
        a = {}
        b = {}
        for c in s:
            a[c] = a.get(c , 0) + 1 
        for ch in t:
            b[ch] = b.get(ch , 0) + 1
        return a == b  
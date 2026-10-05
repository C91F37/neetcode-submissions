class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # let me attempt one pass 
        h = {}
        for s in strs:
            sorted_s = ''.join(sorted(s)) 
            # h[sorted_s] = h.get(sorted_s, []).append(s)
            if sorted_s in h:
                h.get(sorted_s).append(s)
            else:
                h[sorted_s] =[s]
        return list(h.values())
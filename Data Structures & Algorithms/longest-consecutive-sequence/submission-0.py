class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h=set()
        start=[]
        for k in nums:
            h.add(k)   
        for j in h:
            if j-1 not in h:
                start.append(j)
        maxlen = 0        
        for e in start:
            plus=e
            curlen = 0
            while plus in h:
                curlen += 1
                plus+=1
            if curlen > maxlen:
                maxlen = curlen
        return maxlen
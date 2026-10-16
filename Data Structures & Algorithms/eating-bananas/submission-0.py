class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # i am noticing h toujours >= piles
        # donc upper bound of problem is max(piles)
        # lower bound is clearly any k incrementing from 1 that fits the h constraint
        lo,hi = 1, max(piles)
        while lo <= hi:
            g = (lo+hi)//2
            t = 0
            for k in piles:
                t+= -(-k//g)
            if t > h:
                lo=g+1
            else: # t <= h
                hi=g-1
        return lo
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # clean implementation of bucket sort
        # 1. count freq
        h = {}
        for n in nums:
            h[n] = h.get(n, 0) + 1
        # 2. 2d array index = freq, val = list of numbers with this freq
        a = [[] for _ in range(len(nums)+1)]
        for key, val in h.items():
            a[val].append(key)
        ret = []
        for p in range(len(nums), 0, -1):
            ret.extend(a[p])
            if k == len(ret):
                break
        return ret
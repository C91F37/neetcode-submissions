class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ez. we hash map key = nums and val = freq. 
        # we then figure a way out to resolve the k via extracting largest
        h = {}
        for n in nums:
            h[n] = h.get(n, 0) + 1
        # now we have the freq table, i dont have an elegant way to get k
        # but i am sure there is a way to do it
        # one clever way may be to inverse k,v in h
        # another might be importing the counting but i cannae remember the syntax!
        # want to use 2d array for such but then remembered there isnae way to sort cleanly
        r = [[] for i in range(len(nums)+1)]
        # [3][3]
        # [2][2]
        ret = []
        for key in h: 
            r[h.get(key)].append(key) # r[freq] = [nums..]
        # im using a 1d array. but if it is -9999 means there is no number...
        for a in range(len(nums), -1, -1):
            if r[a] == []:
                continue
            for b in r[a]:
                ret.append(b)
            if len(ret) == k:
                break
        return ret
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # l[i] = product of nums[0...i-1]
        # r[i] = product of nums[i+1...n-1]
        ret = []
        n = len(nums) #4
        #n[1,2,3,4]
        #  0 1 2 3
        #l[1,1,2,]
        l, r = [1 for _ in range(n)], [1 for _ in range(n)]
        # l[0] = 1
        i = 1
        while i < n:
            l[i] = l[i-1] * nums[i-1]
            i+=1
        r[n-1] = 1
        i = n-2
        while i > -1:
            r[i] = r[i+1] * nums[i+1]
            i-=1
        for i in range(n):
            ret.append(l[i]*r[i])
        return ret


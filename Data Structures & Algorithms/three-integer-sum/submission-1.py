class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        k = len(nums)-1
        nums.sort()
        res = []
        while i < k:
            k = len(nums)-1
            j=i+1
            if i!=0 and nums[i-1] == nums[i]:
                i+=1
                continue
            while j < k:
                if j!=i+1 and nums[j-1] == nums[j]:
                    j+=1
                    continue
                target = -nums[i] 
                if nums[j] + nums[k] > target: 
                    k -= 1
                    continue
                if nums[j] + nums[k] < target: 
                    j += 1
                    continue
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                j+=1
            i+=1
        return res
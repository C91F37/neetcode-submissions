class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1. L < Mid, Mid > R
        # 2. L > Mid, Mid < R
        # 3. L < Mid < R, or just L < R 
        l = 0
        r = len(nums)-1

        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l+r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1
        return nums[l]
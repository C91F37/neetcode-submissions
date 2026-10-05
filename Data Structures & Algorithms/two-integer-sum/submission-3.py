class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i, x in enumerate(nums):
            h[x] = i
        for i, x in enumerate(nums):
            diff = target - x
            if diff in h and i != h[diff]:
                return [i, h[diff]]
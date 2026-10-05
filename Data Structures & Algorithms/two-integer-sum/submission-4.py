class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={} # diff, i
        for i, x in enumerate(nums):
            diff = target - x
            if diff in h:
                return [h[diff], i]
            h[x] = i
        return []
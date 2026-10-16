class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x,y = 0, len(nums)-1
        while x <= y:
            guess = x+((y-x)//2)
            if nums[guess] < target:
                x = guess + 1
            elif nums[guess] > target:
                y = guess -1
            else:
                return guess
        return -1
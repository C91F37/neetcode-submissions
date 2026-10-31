class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        pivot = -1
        while l < r:
            guess = (l+r)//2
            if nums[l] < nums[r]:
                break
            if nums[l] > nums[r]:
                if nums[guess] > nums[r]:
                    # [l,...g,...pivot, r]
                    l = guess+1
                else:
                    # [l,...pivot,...g, r]
                    r = guess
        pivot = l
        n = len(nums)
        l,r = 0, n-1
        res = -1
        # arr can be accessed by arr[i+p mod n]
        while l <= r:
            guess = (l+r)//2
            i = (guess + pivot) % n
            if nums[i] == target:
                return i
            if nums[i] < target:
                l = guess+1
            else:
                r = guess-1
        return res
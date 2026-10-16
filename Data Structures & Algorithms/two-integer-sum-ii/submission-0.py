class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # inc a if sum less, dec b if sum too much
        a, b = 0, len(numbers) - 1
        res = []
        while a < b:
            if numbers[a] + numbers[b] == target:
                res.append(a+1)
                res.append(b+1)
                return res
            elif numbers[a] + numbers[b] < target:
                a += 1
                continue
            else: 
                b-=1
                continue
        return None
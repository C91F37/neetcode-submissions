class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)

            x = stones[0]
            y = stones[1]
            if x == y:
                stones = stones[2::]
            else:
                if x<y:
                    stones = [y-x] + stones[2::]
                else:
                    stones = [x-y] + stones[2::]
        return stones[0] if stones else 0
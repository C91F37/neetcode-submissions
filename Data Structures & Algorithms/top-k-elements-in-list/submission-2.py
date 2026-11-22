class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        ret = []
        for i in freq.most_common(k):
            ret.append(i[0])
        return ret
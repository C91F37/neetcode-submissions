class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # trying the two pointer solution
        # some feeling told me i can store the indices using a data structure
        # that results in calculation dedupes.
        x,y = 0, len(heights)-1
        area = 0

        while x < y:
            w = y-x
            area = max(w*min(heights[x],heights[y]), area)
            if heights[x] <= heights[y]:
                x+=1
                continue
            else:
                y-=1
                continue
        return area
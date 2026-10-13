class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pos, sorted_speed = zip(*sorted(zip(position, speed), reverse=True))
        stack = []
        time = []
        # for p, s in zip(position, speed): was calculating using original. what a fool i was. 
        for p, s in zip(sorted_pos, sorted_speed):        
            time.append((target-p)/s)
        stack.append(time[0])
        for t in time:
            if t <= stack[-1]:
                continue
            stack.append(t)
        return len(stack)
# 12
# [10,8,5,3,0]
# [2,4,1,3,1]
# [1, 1, 7, 3, 12]
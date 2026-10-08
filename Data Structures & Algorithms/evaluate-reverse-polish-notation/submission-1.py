class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        ops = ['+', '-', '*', '/']
        i = 0
        while i < len(tokens):
            e = tokens[i]
            if e not in ops:
                nums.append(int(e))
                i+=1
                continue
            else:
                y, x = nums.pop(), nums.pop()
                match e:
                    case "*":
                        nums.append(x*y)
                    case "/":
                        nums.append(int(x/y))
                    case "+":
                        nums.append(x+y)
                    case "-":
                        nums.append(x-y)
                i+=1
        return nums[0]
                    
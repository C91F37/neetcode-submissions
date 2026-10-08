class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                opening = stack[-1]
                match opening:
                    case '[':
                        if c != ']':
                            return False
                    case '(':
                        if c != ')':
                            return False
                    case '{':
                        if c != '}':
                            return False
                stack.pop()
        return len(stack)==0
                
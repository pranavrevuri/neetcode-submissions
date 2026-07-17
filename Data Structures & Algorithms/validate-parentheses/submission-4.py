class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if stack and stack[-1] == dict1[c]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
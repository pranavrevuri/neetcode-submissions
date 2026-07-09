class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if stack and stack[-1] == my_dict[char]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0

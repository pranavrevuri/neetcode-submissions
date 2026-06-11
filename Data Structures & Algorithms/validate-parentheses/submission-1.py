class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        mapping_backwards = {'}':'{', ')':'(', ']':'['}

        for char in s:
            if char in mapping_backwards:
                if len(stack_list) != 0 and stack_list[-1] == mapping_backwards[char]:
                    stack_list.pop()
                else:
                    return False
            else:
                stack_list.append(char)
        
        return len(stack_list) == 0

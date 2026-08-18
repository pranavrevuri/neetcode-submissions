class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""
        for digit in range(9, -1, -1):
            target = str(digit) * 3
            if target in num:
                best += target
                break
        
        return best
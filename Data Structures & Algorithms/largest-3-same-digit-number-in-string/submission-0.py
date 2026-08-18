class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""
        for i in range(len(num)-2):
            if num[i] == num[i + 1] == num[i + 2]:
                if not best or num[i] > best[0]:
                    best = 3 * num[i]
        
        return best

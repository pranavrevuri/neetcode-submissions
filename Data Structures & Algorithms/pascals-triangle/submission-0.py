class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = [[] for _ in range(numRows)]


        for i in range(numRows):
            pascals[i].append(1)

            if i != 0:
                for j in range(i - 1):
                    pascals[i].append(pascals[i - 1][j] + pascals[i - 1][j + 1])

                pascals[i].append(1)
        
        return pascals
            

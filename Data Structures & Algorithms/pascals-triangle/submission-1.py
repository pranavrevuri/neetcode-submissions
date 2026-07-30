class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[] for _ in range(numRows)]
        res[0].append(1)

        for i in range(1, numRows):
            res[i].append(1)

            for j in range(i-1):
                res[i].append(res[i-1][j] + res[i-1][j+1])
            res[i].append(1)
        
        return res
            
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for lst in board:
            lst_set = set()
            for digit in lst:
                if digit == '.':
                    continue
                if digit not in lst_set:
                    lst_set.add(digit)
                else:
                    return False
        
        for i in range(len(board)):
            dig_set = set()
            for dig in board:
                if dig[i] == '.':
                    continue
                if dig[i] not in dig_set:
                    dig_set.add(dig[i])
                else:
                    return False

        
        for box in range(len(board)):
            start_row = (box // 3) * 3
            start_col = (box % 3) * 3

            box_set = set()

            for r in range(3):
                for c in range(3):
                    digit = board[start_row + r][start_col + c]
                    if digit == '.':
                        continue
                    if digit not in box_set:
                        box_set.add(digit)
                    else:
                        return False

        return True
                    
        

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid_guess = (left + right) // 2
            pick = guess(mid_guess)

            if pick == 0:
                return mid_guess
            elif pick == 1:
                left = mid_guess + 1
            else:
                right = mid_guess - 1
        

        
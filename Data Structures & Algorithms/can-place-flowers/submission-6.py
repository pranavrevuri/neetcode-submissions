class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        count = 0

        for i in range(l):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or flowerbed[i - 1] == 0
                right_empty = (i == l - 1) or flowerbed[i + 1] == 0

                if left_empty and right_empty:
                    count += 1
                    flowerbed[i] = 1

        
        return count >= n

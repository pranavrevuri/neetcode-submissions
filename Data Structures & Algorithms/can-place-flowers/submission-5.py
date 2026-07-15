class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        can_plant = 0
        
        if n == 0:
            return True
        if l == 1:
            return flowerbed[0] == 0

        for i in range(l):
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i+1] == 0:
                    can_plant += 1
                    flowerbed[i] = 1
                elif i == l - 1:
                    if flowerbed[i-1] == 0:
                        can_plant += 1
                        flowerbed[i] = 1
                elif i != l - 1:
                        if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                            can_plant += 1
                            flowerbed[i] = 1

        
        return can_plant >= n
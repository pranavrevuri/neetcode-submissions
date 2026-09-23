class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        unique = 1
        
        pairs = list(zip(position, speed))
        pairs = sorted(pairs, key=lambda p: p[0], reverse=True)

        fleet_time = (target - pairs[0][0]) / pairs[0][1]
        for i in range(1, n): 
            time = (target - pairs[i][0]) / pairs[i][1]
            if time > fleet_time:
                unique += 1
                fleet_time = time
        
        return unique
        

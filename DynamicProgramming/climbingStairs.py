# Climbing Stairs(1) = 1
# Climbing Stairs(2) = 2
# Climbing Stairs(3) = 3
# Climbing Stairs(4) = 5
# Climbing Stairs(5) = 8
# Climbing Stairs(n) = Climbing Stairs(n-1) + Climbing Stairs(n-2)

def climbingStairs(n: int) -> int:
    cache = {}
    def climb(stair):
        # base case
        if stair <= 2:
            return stair
        if stair in cache:
            return cache[stair]
        # recursive case
        answer = climb(stair-1) + climb(stair-2 )
        cache[stair] = answer
        return answer
    
    return climb(n)

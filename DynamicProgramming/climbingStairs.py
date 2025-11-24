# Climbing Stairs(1) = 1
# Climbing Stairs(2) = 2
# Climbing Stairs(3) = 3
# Climbing Stairs(4) = 5
# Climbing Stairs(5) = 8
# Climbing Stairs(n) = Climbing Stairs(n-1) + Climbing Stairs(n-2)

def climbingStairs(n: int) -> int:

    # base case
    if n <=2:
        return n
    # recursive case
    return climbingStairs(n-1) + climbingStairs(n-2)
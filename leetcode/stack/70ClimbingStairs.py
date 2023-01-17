# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            fib = [0] * (n + 1)
            fib[0] = 1
            fib[1] = 1
            for i in range(2, n + 1):
                fib[i] = fib[i-1] + fib[i-2]
            return fib[n]
        

print(Solution().climbStairs(2)) # 2
print(Solution().climbStairs(3)) # 3
print(Solution().climbStairs(4)) 
print(Solution().climbStairs(5)) 
print(Solution().climbStairs(6))

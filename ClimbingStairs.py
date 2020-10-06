"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

"""
import math
class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 1
        maxTwos = n//2
        for i in range(1,maxTwos+1):
            ways +=  math.factorial(n-i)/(math.factorial(i) * math.factorial(n-(2*i)))
            
        return int(ways)

sol = Solution()
print(sol.climbStairs(5))
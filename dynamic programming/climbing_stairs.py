def climbStairs(n):
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr

print(climbStairs(3))

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        one_before = 1
        two_before = 1
        total = 0
        for i in range(2, n+1):
            total = one_before + two_before
            two_before = one_before
            one_before = total
        return total
        
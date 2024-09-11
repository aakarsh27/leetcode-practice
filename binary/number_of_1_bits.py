class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(32):
            if (n >> i) & 1:
                res += 1

class Solution2:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
        
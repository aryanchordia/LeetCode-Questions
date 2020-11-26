class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        if x > 0:
            s = str(x)
            r = int(s[::-1])
            if r < pow(-2,31) or r > pow(2,31) - 1:
                return 0
            return r
        x = -x
        s = str(x)
        r = int(s[::-1])
        if r < pow(-2,31) or r > pow(2,31) - 1:
                return 0
        return -r

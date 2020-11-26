class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        if n == 0:
            return 1
        subresult = self.myPow(x, n//2)
        if n % 2 == 0:
            return subresult * subresult
        else:
            return subresult * subresult * xa
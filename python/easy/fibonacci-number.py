"""
Link: https://leetcode.com/problems/fibonacci-number/
"""

class Solution:
    def __init__(self):
        self.cache = {}

    def fib(self, n: int) -> int:
        if n<=1:
            return n
        else:
            if n in self.cache:
                return self.cache[n]
            else:
                res = self.fib(n-1) + self.fib(n-2)
                self.cache[n] = res
            return res
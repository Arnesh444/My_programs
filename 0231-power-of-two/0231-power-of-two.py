class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        a=bin(n)
        return (a.count('1')==1)
        
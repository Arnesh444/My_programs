class Solution(object):
    def hammingWeight(self, n):
        a=str(bin(n))
        return a.count('1')
        
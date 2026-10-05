class Solution(object):
    def findNumbers(self, nums):
        a=list(filter(lambda x:len(str(x))%2==0, nums))
        return len(a)
        
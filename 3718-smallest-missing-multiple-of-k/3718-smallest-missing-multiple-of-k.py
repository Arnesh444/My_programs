class Solution(object):
    def missingMultiple(self, nums, k):
        a=1
        for i in range(len(nums)+1):
            n=a*k

            if n not in nums:
                return n

            a+=1


        
class Solution(object):
    def largestInteger(self, nums, k):
        count = {}
        for i in range(len(nums)-k+1):
            sub=set(nums[i:i+k])

            for x in sub:
                count[x] = count.get(x,0) + 1

        an=-1

        for x in count:
            if count[x]==1:
                an=max(an,x)
        return an
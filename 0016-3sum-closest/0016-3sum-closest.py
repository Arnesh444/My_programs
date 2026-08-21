class Solution(object):
    def threeSumClosest(self, nums, target):
       nums.sort()
       re=nums[0]+nums[1]+nums[2]

       for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue

        j=i+1
        k=len(nums)-1
        while j<k:
            tot=nums[i]+nums[j]+nums[k]

            if tot==target:
                return tot

            if abs(target-tot)<abs(target-re):
                re=tot

            if tot>target:
                k-=1

            if tot<target:
                j+=1

       return re    
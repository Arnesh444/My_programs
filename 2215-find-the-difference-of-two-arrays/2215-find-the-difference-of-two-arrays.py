class Solution(object):
    def findDifference(self, nums1, nums2):
        a=[]
        b=list(set(nums1)-set(nums2))
        a.append(b)
        c=list(set(nums2)-set(nums1))
        a.append(c)

        return a

        
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
       me=nums1+nums2
       me.sort()
       a=0

       x=len(me)
       if x%2==0:
        a=float((me[x//2]+me[(x//2)-1]))/2
       else:
        a=me[x//2]
       return a 

class Solution(object):
    def intersect(self, nums1, nums2):
        a=set(nums1)
        b=set(nums2)
        l=[]

        for x in a:
            if x in b:
                n=min(nums1.count(x),nums2.count(x))
                
                for i in range(n):
                    l.append(x)

        
        return l

        



        
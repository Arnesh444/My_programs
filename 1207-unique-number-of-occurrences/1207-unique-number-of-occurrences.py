class Solution(object):
    def uniqueOccurrences(self, arr):
        a=set(arr)
        l=[]
        c=0

        for x in a:
            l.append(arr.count(x))

        if len(set(l))==len(l):
            return True
        else:
            return False
        
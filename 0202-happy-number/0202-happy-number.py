class Solution(object):
    def isHappy(self, n):
        seen=set()

        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            s=0

            while n>0:
                m=n%10
                s+=(m**2)
                n=n//10

            n=s
        
        return True

        
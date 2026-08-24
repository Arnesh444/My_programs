class Solution(object):
    def isPalindrome(self, s):
        r=""
        s=s.lower()

        for c in s:
            if c.isalnum()==True:
                r+=c

        a=r[::-1]

        if a==r:
            return True
        if r=="":
            return True
        else:
            return False
        
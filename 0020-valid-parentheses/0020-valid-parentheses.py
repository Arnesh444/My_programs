class Solution(object):
    def isValid(self, s):
       p={"(": ")","{":"}","[":"]"}
       a=[]

       for c in s:
        if c in "({[":
            a.append(c)

        else:
            if len(a)==0:
                return False
            if p[a[-1]]==c:
                a.pop()
            else:
                return False

       return len(a)==0   
        
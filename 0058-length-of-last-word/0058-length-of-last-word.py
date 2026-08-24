class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        c=0
        x=len(s)-1
        r=""
        if len(s)==1:
            return len(s)

        for i in range(x,-1,-1):
            if s[i]!=' ':
                r+=s[i]
            else:
                break

        return len(r)



        
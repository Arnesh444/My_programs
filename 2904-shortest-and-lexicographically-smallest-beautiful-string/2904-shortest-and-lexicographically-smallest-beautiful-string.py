class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        a=[]
        su=0
        r=""
        for i in range(len(s)):
            su+=int(s[i])
            r+=s[i]
            if su==k:
                while r[0]=="0":
                    r=r[1:]

                a.append(r)
                r=r[1:]
                su-=1

        if len(a)==0:
            return ""

        b=min(a, key=lambda x:(len(x), x))

        return b
            
       
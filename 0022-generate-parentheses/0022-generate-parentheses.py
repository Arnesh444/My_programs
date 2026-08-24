class Solution(object):
    def generateParenthesis(self, n):
        a=[]

        def ba(s,op,cl):

            if len(s)==2*n:
                a.append(s)
                return

            if op<n:
                ba(s+ "(",op+1,cl)
            if cl<op:
                ba(s+")",op,cl+1)

        ba("",0,0)

        return a
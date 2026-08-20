class Solution(object):
    def letterCombinations(self, digits):
        count={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        s=[""]
        
        for digit in digits:
            le=count[digit]
            new=[]

            for word in s:
                for ch in le:
                    new.append(word+ch)
            s=new
        
        return s
            

                

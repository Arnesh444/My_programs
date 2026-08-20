class Solution(object):
    def myAtoi(self, s):
        og=s.strip()
        lo=""
        for i in range(len(og)) :
         if og[i].isdigit()==True or ((og[i]=="-" or og[i]=="+") and i==0) :
          lo+=og[i]
         else:
            break

        if lo=="" or lo=="-" :
            return 0

        num=0
        
        for ch in lo :
            if ch.isdigit():
                num=num*10 + int(ch)

        if lo[0]=="-" :
            num=-num
            
        if num<-2**31:
            num=-2**31
        if num>2**31-1:
            num=2**31-1
        
        return num

        
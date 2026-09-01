class Solution(object):
    def uniqueMorseRepresentations(self, words):
        a=[]
        d={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        r=""
        for word in words:
            for ch in word:
                r+=d[ch]
            a.append(r)
            r=""
        
        return len(set(a))
        
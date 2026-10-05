class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        a=sum(aliceSizes)
        b=sum(bobSizes)

        di=(b-a)//2

        for x in aliceSizes:
            y=x+di
            if y in bobSizes:
                return [x,y]
        
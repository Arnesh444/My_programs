class Solution(object):
    def maxArea(self, height):
      max=0
      i=0
      j=len(height)-1

      while i<j:
        a=(j-i)*min(height[i],height[j])

        if a>max:
            max=a

        if height[i]<height[j]:
            i+=1
        else:
            j-=1

      return max  
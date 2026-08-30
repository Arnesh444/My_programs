class Solution(object):
    def minimumDeletions(self, nums):
        a=max(nums)
        in1=nums.index(a)+1
        b=min(nums)
        in2=nums.index(b)+1
        sum=0

        if len(nums)==1:
            return 1
        elif len(nums)>1 and in2>in1:
            in22=len(nums)-in2+1
            in11=len(nums)-in1+1
            sum=in1+in22
            return min(sum,in2,in11)
        elif len(nums)>1 and in2<in1:
            in11=len(nums)-in1+1
            in22=len(nums)-in2+1
            sum=in11+in2
            return min(sum,in1,in22)

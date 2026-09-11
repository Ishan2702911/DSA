class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum=nums[0]
        max_sum=nums[0]
        curr_max=nums[0]
        curr_min=nums[0]
        for i in range(1,len(nums)):
            x=nums[i]
            curr_max=(max(x,curr_max+x))
            max_sum=max(curr_max,max_sum)
            curr_min=min(x,curr_min+x)
            min_sum=min(curr_min,min_sum)
        return max(abs(min_sum),abs(max_sum)) 
        
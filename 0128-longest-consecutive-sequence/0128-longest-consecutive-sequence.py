class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        lenght=1
        max_lenght=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue 
            if nums[i]-nums[i-1]==1:
                lenght+=1
                if lenght>max_lenght:
                    max_lenght=lenght
            else:
                lenght=1
        return max_lenght
            
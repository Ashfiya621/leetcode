# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        h=n
        ans=-1
        while l<=h:
            mid=l+(h-l)//2
            res=isBadVersion(mid)

            if res==True:
                ans=mid
                h=mid-1

            else:
                l=mid+1

        return ans

        
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=0
        for (k,v) in count.items():
            if v==1:
                ans+=k
        return ans

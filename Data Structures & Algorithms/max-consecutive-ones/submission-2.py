class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    
        cnt = 0
        save = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else: 
                if save < cnt:
                    save = cnt
                cnt = 0

        return max(cnt, save)
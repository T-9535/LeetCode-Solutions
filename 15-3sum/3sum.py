class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        s = set()
        for i in range(n-2):
            #new_target = target-nums[i]
            left = i+1
            right = n-1
            while left< right:
                current_sum  = +nums[i]+nums[left]+nums[right]
                if current_sum <0:
                    left+=1
                elif current_sum>0:
                    right-=1
                else:
                    s.add((nums[i], nums[left], nums[right]))
                    left+=1
                    right-=1
        return [list(x) for x in s]

        
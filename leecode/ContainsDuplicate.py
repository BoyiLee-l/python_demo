from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = {}
        for i in nums:
            if i not in numset:
                numset[i] = 1
                print(f"set: {numset}")
            else:
                return True
        return False

solution = Solution()
nums = [1,2,3,1]
print(solution.containsDuplicate(nums))

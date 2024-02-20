from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes, count = 0, 0
        # Find potential majority element
        for num in nums:
            if votes == 0:
                x = num
            if num == x:
                votes += 1
            else:
                votes -= 1

            print(f"votes: {num}, {x}, {votes}")   
        # Validate if x is the majority element
        for num in nums:
            if num == x:
                count += 1

            print(f"數量：{count}")   

        if count > len(nums) // 2:
            result = x
        else:
            result = 0

        print(result)
        return result

solution = Solution()
nums = [3,2,2,1,1,1,2,2,2]
solution.majorityElement(nums)

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# 題目說明
# 1. 題目要求在一個排序好的list中找到指定的數字
# 2. 如果找到就回傳該數字的index
# 3. 如果沒有找到就回傳該數字應該要插入的index


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
            else:
                i += 1
        return i

if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 5
    print(Solution().searchInsert(nums, target))
    nums = [1,3,5,6]
    target = 2
    print(Solution().searchInsert(nums, target))
    nums = [1,3,5,6]
    target = 7
    print(Solution().searchInsert(nums, target))
    nums = [1,3,5,6]
    target = 0
    print(Solution().searchInsert(nums, target))
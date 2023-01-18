# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# 題目說明：給定一個整數數組nums和一個整數目標(target)，返回兩個數字的"索引"，使它們相加到目標。


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 用暴力法的方法
        # self: 代表的是類的實例，而非類, 代表的是當前對象的地址
        for i in range(len(nums)):
            # for i in range(len(nums)): 這個判斷式的意思是，將nums裡面的元素一個一個取出來，並且將它們的索引值一個一個取出來，並且將它們的索引值和元素一一對應起來，並且將它們存放在i裡面。
            for j in range(i+1,len(nums)):
                # i+1: key+1的意思是，將i的值加1，並且將它們的索引值和元素一一對應起來，並且將它們存放在j裡面。
                # for j in range(i+1,len(nums)): 這個判斷式的意思是，將nums裡面的元素一個一個取出來，並且將它們的索引值一個一個取出來，並且將它們的索引值和元素一一對應起來，並且將它們存放在j裡面。
                if nums[i]+nums[j]==target:
                    # if nums[i]+nums[j]==target: 這個判斷式的意思是，如果nums[i]+nums[j]==target，就回傳[i,j]
                    return [i,j]

# 第一次檢討
# 忘了打len len: 代表的是長度
# if nums[i] + nums[j] == target: 兩個==沒打到 

nums = [2,7,11,15]
target = 26
print(Solution().twoSum(nums,target))

nums = [3,2,4]
target = 6
print(Solution().twoSum(nums,target))

nums = [3,3]
target = 6
print(Solution().twoSum(nums,target))


# 用hash table的方法
class Solution:
    def twoSum(self, nums, target):
        hash_map = {}
        for i, num in enumerate(nums):
            # for i, num in enumerate(nums): 這個判斷式的意思是，將nums裡面的元素一個一個取出來，並且將它們的索引值一個一個取出來，並且將它們的索引值和元素一一對應起來，並且將它們存放在hash_map裡面。
            # enumerate() 函數用於將一個可遍歷的數據對象(如列表、元組或字符串)組合為一個索引序列，同時列出數據和數據下標，一般用在 for 循環當中。
            if target - num in hash_map:
                # if target - num in hash_map: 這個判斷式的意思是，如果target-num在hash_map裡面，就回傳hash_map[target-num]和i
    
                return [hash_map[target - num], i]
                
# 這段程式碼判斷 hash_map 中是否有 target-num 這個值，如果有，則返回一個包含 hash_map 中 target-num 對應值(即在輸入陣列 nums 中與當前數 num 相加為 target 的那個數的索引) 和當前的索引 i 的列表。
# 這樣的判斷在 hash_map 中找到另一個數字，使得它與當前的 num 相加等於目標值，那麼這兩個數字的索引就是所求的答案。
                
            hash_map[num] = i
            # hash_map[num] = i 這個判斷式的意思是，如果target-num不在hash_map裡面，就將num和i存放在hash_map裡面。
            
        return None

# 第一次檢討
# enumerate要知道的是，它是一個函數，它的作用是將一個可遍歷的數據對象(如列表、元組或字符串)組合為一個索引序列，同時列出數據和數據下標，一般用在 for 循環當中。

nums = [2,7,11,15,3]
target = 18
print (Solution().twoSum(nums,target))

nums = [3,2,4]
target = 6
print (Solution().twoSum(nums,target))

nums = [3,3]
target = 6
print (Solution().twoSum(nums,target))

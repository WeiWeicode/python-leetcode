# twosum範例
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
# 這個範例是一個簡單的暴力解法，它有一個 twoSum 方法，用來找出兩個數字的索引，使得這兩個數字的總和等於 target。
# 這個 twoSum 方法有兩個參數，nums 是一個整數的陣列，target 是一個整數。
# 這個 twoSum 方法會回傳一個整數的陣列，這個陣列中有兩個元素，分別是兩個數字的索引。
i = Solution()
print(i.twoSum([2, 7, 11, 15], 9))
# 這個範例是一個簡單的暴力解法，它有一個 twoSum 方法，用來找出兩個數字的索引，使得這兩個數字的總和等於 target。

# 列出步驟
# 1. 建立一個 Solution 類別
# 2. 在 Solution 類別中定義一個 twoSum 方法，這個方法有兩個參數，nums 和 target
# 3. 在 twoSum 方法中，使用 for 迴圈，將 nums 中的每個元素取出，並將它的索引存到變數 i 中
# 4. 在 twoSum 方法中，使用 for 迴圈，將 nums 中的每個元素取出，並將它的索引存到變數 j 中
# 5. 在 twoSum 方法中，判斷 nums[i] 和 nums[j] 的總和是否等於 target
# 6. 如果 nums[i] 和 nums[j] 的總和等於 target，則回傳 [i, j]
# 7. 建立一個 Solution 類別的實例
# 8. 呼叫 Solution 類別的實例的 twoSum 方法，並將 [2, 7, 11, 15] 和 9 傳入 twoSum 方法中
# 9. 印出 [0, 1]



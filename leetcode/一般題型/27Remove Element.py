# 27. Remove Element
# Easy
# 5.2K
# 6.9K
# Companies
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# 題目說明
# 1. 題目要求在原本的list上面刪除指定的數字
# 2. 題目要求刪除後的list要保持原本的順序
# 3. 題目要求刪除後的list要保持原本的長度

# 解題思路
# 1. 這題的解題思路是用兩個指針，一個指向原本的list，一個指向新的list
# 2. 如果原本的list的值不等於指定的數字，就把原本的list的值放到新的list上面
# 3. 最後回傳新的list的長度

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

if __name__ == "__main__":
    s = Solution()
    print(s.removeElement([3,2,2,3], 3))
    print(s.removeElement([0,1,2,2,3,0,4,2], 2))

# 給定一個整數陣列 nums 和一個整數 val，在原地移除 nums 中所有出現過的 val。元素的相對順序可能會改變。

# 由於在某些語言中無法改變陣列的長度，因此您必須將結果放在陣列 nums 的第一部分中。
# 更正式地說，如果在刪除重複項後有 k 個元素，則 nums 的前 k 個元素應包含最終結果。
# 您在第一個 k 個元素之後留下的東西並不重要。

# 在第一個 k 個槽中置入最終結果後，返回 k。

# 不要為另一個陣列分配額外的空間。您必須通過用 O(1) 額外的記憶體修改輸入陣列來實現這一點。
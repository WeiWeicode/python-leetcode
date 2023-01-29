# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.





# # nums1 = [1,3]
# # nums2 = [2]

# nums1 = [1,2]
# nums2 = [3,4]

# nums1.extend(nums2)
# print (nums1)
# # extend: 會將nums2的元素加入nums1

# nums1.sort()
# print (nums1)
# # sort: 會將原本的list排序

# if len(nums1) % 2 == 0:
#     print((nums1[len(nums1)//2] + nums1[len(nums1)//2 - 1])/2)
# else:
#     print(nums1[len(nums1)//2])

# Path: leetcode\一般題型\04Median of Two Sorted Arrays.py

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            return (nums1[len(nums1)//2] + nums1[len(nums1)//2 - 1])/2
        else:
            return nums1[len(nums1)//2]
# %: 取餘數
# //: 取整數

if __name__ == '__main__':
    nums1 = [1,3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))
    nums1 = [1,2]
    nums2 = [3,4]
    print(Solution().findMedianSortedArrays(nums1, nums2))
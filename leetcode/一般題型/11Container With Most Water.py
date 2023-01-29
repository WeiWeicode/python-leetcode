# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1


from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1. 暴力法
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         max_area = max(max_area, min(height[i], height[j]) * (j-i))
        # return max_area

        # 2. 雙指針
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))
    height = [1,1]
    print(Solution().maxArea(height))


# 這段程式碼是計算一個數組中最大面積的程式碼。它是使用双指针法來實現的。變量 left 和 right 分別表示指向數組頭尾的兩個指針。

# 在迴圈中，計算當前面積（由 min(height[left], height[right]) * (right - left) 計算）並與現有的最大面積（max_area）比較。如果當前面積比最大面積大，則將其賦值給最大面積。

# 接下來，如果左指針指向的高度小於右指針指向的高度，則將左指針右移一位。否則，將右指針左移一位。

# 這樣做可以保證我們縮小範圍，並在最終返回最大面積。最後用main中兩組數測試。
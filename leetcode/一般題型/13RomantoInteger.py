# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.



class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        
        for i in range(len(s)):            
            if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                result += roman[s[i]] - 2 * roman[s[i - 1]]
                
                # print (i)
                # print (roman[s[i]])
                # print (roman[s[i - 1]])
                
            else:
                result += roman[s[i]] 


        return result




if __name__ == '__main__':
    s = "MCMXCIV"
    print(Solution().romanToInt(s))




# print (0 > 0 and 1000 > 0) 
# print (1 > 0 and 100 > 1000)
# print (2 > 0 and 1000 > 100)
# print (3 > 0 and 10 > 1000)
# pinrt (4 > 0 and 100 > 10)
# print (5 > 0 and 1 > 100)
# pirnt (6 > 0 and 5 > 1)

print (2 > 0)
print (1000 > 100)

# 第一步0>0 false
# 第二步100>1000 false
# 第三步1000>100 true
# 第四步10>1000 false
# 第五步100>10 true
# 第六步1>100 false
# 第七步5>1 true

# 結論 比對and後面
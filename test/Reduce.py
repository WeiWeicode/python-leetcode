from functools import reduce
 
nums = [1, 2, 3, 4, 5]
sum_nums = reduce(lambda x, y: x+y, nums)

print("The sum is {}".format(sum_nums))

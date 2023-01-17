# Original object
original_list = [1, 2, [3, 4]]

# Shallow copy
shallow_copy_list = original_list.copy()

# Deep copy
import copy
deep_copy_list = copy.deepcopy(original_list)

# Modify the original list
original_list[2][0] = 'new value'

# Check the original list and the shallow copy
print("Original list:", original_list)
# Output: Original list: [1, 2, ['new value', 4]]
print("Shallow copy:", shallow_copy_list)
# Output: Shallow copy: [1, 2, ['new value', 4]]

# Check the original list and the deep copy
print("Original list:", original_list)
# Output: Original list: [1, 2, ['new value', 4]]
print("Deep copy:", deep_copy_list)
# Output: Deep copy: [1, 2, [3, 4]]

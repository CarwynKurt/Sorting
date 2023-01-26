# Defines Merge Sort
def merge_sort(nums):
    # Divide Array
    if len(nums) > 1:
        left_array = nums[:len(nums) // 2]
        right_array = nums[len(nums) // 2:]

    # Recursion
        merge_sort(left_array)
        merge_sort(right_array)

# Merge
# Present Array Values
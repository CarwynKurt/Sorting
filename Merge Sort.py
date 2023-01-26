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
        i = 0
        j = 0
        k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                nums[k] = left_array[i]
                i += 1
            else:
                nums[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            nums[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            nums[k] = right_array[j]
            j += 1
            k += 1

        print(nums)

# Present Array Values
nums = [82, 24, 25, 12, 34, 26, 94, 55, 71, 8]
merge_sort(nums)

print(nums)
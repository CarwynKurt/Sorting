# Define Quick Sort
def quick_sort(nums, left, right):
    if left < right:
        partition_pos = partition(nums, left, right)
        quick_sort(nums, left, partition_pos - 1)
        quick_sort(nums, partition_pos + 1, right)

# Define Partition
def partition(nums, left, right):
    i = left
    j = right - 1
    pivot = nums[right]

    # While Loop
    while i < j:
        while i < right and nums[i] < pivot:
            i += 1
        while j > left and nums[j] >= pivot:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    if nums[i] > pivot:
        nums[i], nums[right] = nums[right], nums[i]

    print(nums)
    return i

# Present Array Values
nums = [82, 24, 25, 12, 34, 26, 94, 55, 71, 8]
quick_sort(nums, 0, len(nums) - 1)

print(nums)
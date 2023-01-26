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
# Present Array Values

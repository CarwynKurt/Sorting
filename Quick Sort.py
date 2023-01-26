# Define Quick Sort
def quick_sort(nums, left, right):
    if left < right:
        partition_pos = partition(nums, left, right)
        quick_sort(nums, left, partition_pos - 1)
        quick_sort(nums, partition_pos + 1, right)

# Define Partition
# While Loop
# Present Array Values

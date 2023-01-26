# Define Insertion Sort
def insertion_sort(nums):
    # Create Nested Loop
    for i in range(1, len(nums)):
        anchor = nums[i]
        j = i - 1
        while j >= 0 and anchor < nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = anchor

        print(nums)

# Present Array Values
nums = [82, 24, 25, 12, 34, 26, 94, 55, 71, 8]
insertion_sort(nums)

print(nums)
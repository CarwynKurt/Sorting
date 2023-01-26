# Define Sort
def sort(nums):

    # Create Nested Loop
    for i in range(9):
        minpos = i
        for j in range(i, 10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

# Present Array Values
nums = [82, 24, 25, 12, 34, 26, 94, 55, 71, 8]
sort(nums)

print(nums)
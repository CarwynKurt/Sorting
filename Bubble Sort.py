# Define Sort
def sort(nums):

    # Create Nested Loop
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

                print(nums)

# Present Array Values
nums = [82, 24, 25, 12, 34, 26, 94, 55, 71, 8]
sort(nums)

print(nums)
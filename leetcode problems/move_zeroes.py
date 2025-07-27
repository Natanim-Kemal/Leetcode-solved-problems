def move_zeroes(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        return nums

move_zeroes([0, 1, 0, 3, 4, 0, 2, 8, 12])


for i in range(10):
    print(i, end=' ')
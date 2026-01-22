def insertion_sort_psuedocode(nums):

    for i in range(len(nums)):
        j = i

        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1

    return nums

def insertion_sort(nums: list[int]):
    for i in range(1, len(nums)):
        j = i - 1
        num = nums[i]

        while j >= 0 and nums[j] > num:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = num

    return nums

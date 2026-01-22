def bubble_sort_pseudocode(nums):
    swapping = True
    end = len(nums)

    while swapping:
        swapping = False

        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True

        end -= 1

    return nums


def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        swapping = False

        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapping = True

        if not swapping:
            break

    return nums

def find_minimum(nums):
    if len(nums) == 0:
        return None

    minimum = float("inf")

    for num in nums:
        if num < minimum:
            minimum = num
    return minimum


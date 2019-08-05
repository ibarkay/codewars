def checkio(*nums):
    if len(nums) == 0:
        return 0
    else:
        return max(nums) - min(nums)


checkio(10.2, -2.2, 0, 1.1, 0.5)
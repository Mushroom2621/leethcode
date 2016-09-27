def twoSum(nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    nums: List[int]
    target: int
    return a list of length two indicating the index of the two numbers which sum equals to target

    >>> twoSum([3, 2, 4], 6)
    [1, 2]
    """
    ht = dict()
    for i in range(len(nums)):
        if ht.has_key(nums[i]):
            return [ht[nums[i]], i]
        else:
            ht[target - nums[i]] = i
    return [0, 0]

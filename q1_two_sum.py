# find the indices for two elements that add up to Target
def run(nums, target):
    """
    # type: List[int]
    # type: target
    # rtype: List[int, int]
    """

    prev_map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return 
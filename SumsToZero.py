def find_nums(nums):
    output = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    existed = False
                    for element in output:
                        if sorted(element) == sorted([nums[i], nums[j], nums[k]]):
                            existed = True
                    if not existed:
                        output.append([nums[i], nums[j], nums[k]])
    return output


print(find_nums([-1, 0, 1, 2, -1, -4]))

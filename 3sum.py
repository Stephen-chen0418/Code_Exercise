class Solution(object):
    def binarySearch(self, array):
        m = len(array)
        a = []
        for j in range(m):
            if len(a) == 0:
                a.append(array[j])
            else:
                start = 0
                end = len(a) - 1
                pos = 0
                while start <= end:
                    mid = start + (end - start) // 2
                    if a[mid] == array[j]:
                        a.insert(max(0, mid + 1), array[j])
                        break
                    elif a[mid] > array[j]:
                        pos = end = mid - 1
                    else:
                        pos = start = mid + 1
                    if start > end:
                        pos = start
                        a.insert(max(0, pos), array[j])
                        break
        return a

    def threeSum(self, nums):
        n = len(nums)
        result = []
        nums = self.binarySearch(nums)

        for i in range(n - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue
            if 0 < i and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    while l < r - 1 and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                elif tmp < 0:
                    l += 1
                else:
                    r -= 1
        return result
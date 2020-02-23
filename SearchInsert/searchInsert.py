class Solution:
    def searchInsert(self, nums, target):
        length = len(nums)
        if length == 1:
            if nums[0]<target:
                return length
            else:
                return length - 1 #Return 0
        for i in range(length):
            if not nums[i]< target:
                break
        if i == length - 1:
            if nums[i] == target:
                return i
            if target > nums[i]:
                return  i + 1
        return i


sol = Solution()
print(sol.searchInsert([1,3], 2))

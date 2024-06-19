class Solution(object):
    def twoSum(self, nums, target):
        result_all = {}
        for x1, x2 in enumerate(nums):
            if target - x2 in result_all:
                return [result_all[target - x2], x1]
            result_all[x2] = x1
        return []

############示例用法
solution=Solution()
nums=[2,8,0,7,11,15]
target=9
print(solution.twoSum(nums,target))#输出:[0,1]

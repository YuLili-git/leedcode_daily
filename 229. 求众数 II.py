#给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
#示例 1：
#输入：[3,2,3]
#输出：[3]
#示例 2：
#输入：nums = [1]
#输出：[1]
#示例 3：
#输入：[1,1,1,3,3,2,2,2]
#输出：[1,2]
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        res = []
        for i,j in dic.items():
            if j > n:
                res.append(i)
        return res

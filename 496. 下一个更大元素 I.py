#给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
#请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
#nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
#示例 1:
#输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
#输出: [-1,3,-1]
#解释:
#    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
#    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
#    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
#示例 2:
#输入: nums1 = [2,4], nums2 = [1,2,3,4].
#输出: [3,-1]
#解释:
#    对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
#    对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
################################# solution 1 #################################
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tmp = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            tmp.append(nums2[k])
                            break
            if len(tmp) != i + 1:
                tmp.append(-1)
        return tmp 
################################# solution 2 #################################
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tmp = {}
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    tmp[nums2[i]] = nums2[j]
                    break
            if len(tmp) != i + 1:
                tmp[nums2[i]] = -1
        res = []
        for i in nums1:
            res.append(tmp[i])
        return res
################################# solution 3 #################################
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            if stack:
                res[num] = stack[-1]  
            else: 
                res[num] = -1
            stack.append(num)
        return [res[num] for num in nums1]

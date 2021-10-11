#给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
#示例 1：
#输入：[3, 2, 1]
#输出：1
#解释：第三大的数是 1 。
#示例 2：
#输入：[1, 2]
#输出：2
#解释：第三大的数不存在, 所以返回最大的数 2 。
#示例 3：
#输入：[2, 2, 3, 1]
#输出：1
#解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
#此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。
#################################### solution 1 ####################################
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        pq = []
        for num in set(nums):
            heapq.heappush(pq, num)
            if len(pq) > 3:
                heapq.heappop(pq)
        if len(pq) == 3:
            return heapq.heappop(pq)  
        else: 
            return pq[-1]
          

#################################### solution 1 ####################################          
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        def quick_sort(l, r, arr):
            if l >= r:
                return
            i = l 
            j = r 
            while i < j:
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                while i < j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[l] = arr[l], arr[i]
            quick_sort(l, i - 1, arr)
            quick_sort(i + 1, r, arr)
            return arr
        quick_sort(0, len(nums) - 1, nums)
        
        num = []
        for i in nums:
            if i not in num:
                num.append(i)

        if len(num) < 3:
            return num[-1]
        else:
            return num[-3]
         
  

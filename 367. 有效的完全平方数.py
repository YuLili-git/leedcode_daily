#给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
#进阶：不要 使用任何内置的库函数，如  sqrt 。
#示例 1：
#输入：num = 16
#输出：true
#示例 2：
#输入：num = 14
#输出：false
#提示：
#1 <= num <= 2^31 - 1
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            target = (left + right) // 2
            if target * target == num:
                return True
            elif target * target < num:
                left = target + 1
            else:
                right = target - 1
        return False

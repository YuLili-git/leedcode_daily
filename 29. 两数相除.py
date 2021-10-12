#给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#返回被除数 dividend 除以除数 divisor 得到的商。
#整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
#示例 1:
#输入: dividend = 10, divisor = 3
#输出: 3
#解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
#示例 2:
#输入: dividend = 7, divisor = -3
#输出: -2
#解释: 7/-3 = truncate(-2.33333..) = -2
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_min, int_max = -2**31, 2**31 - 1
        
        if dividend == int_min:
            if divisor == 1:
                return int_min
            if divisor == -1:
                return int_max

        if divisor == int_min:
            if dividend == int_min:
                return 1
            else:
                return 0
        
        if dividend == 0:
            return 0

        rev = False
        if dividend > 0:
            dividend = - dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        def quick_add(y, z, x):
            result, add = 0, y
            while z > 0:
                if (z & 1) == 1:
                    if result < x - add:
                        return False
                    result += add
                if z != 1:
                    if add < x - add:
                        return False
                    add += add
                z >>= 1
            return True
        
        left, right, ans = 1, int_max, 0
        while left <= right:
            mid = left + ((right - left) >> 1)
            check = quick_add(divisor, mid, dividend)
            if check:
                ans = mid
                if mid == int_max:
                    break
                left = mid + 1
            else:
                right = mid - 1
        
        if rev:
            return -ans
        else:
            return ans


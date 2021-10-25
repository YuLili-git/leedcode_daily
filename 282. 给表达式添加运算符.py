#给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。
#示例 1:
#输入: num = "123", target = 6
#输出: ["1+2+3", "1*2*3"] 
#示例 2:
#输入: num = "232", target = 8
#输出: ["2*3+2", "2+3*2"]
#示例 3:
#输入: num = "105", target = 5
#输出: ["1*0+5","10-5"]
#示例 4:
#输入: num = "00", target = 0
#输出: ["0+0", "0-0", "0*0"]
#示例 5:
#输入: num = "3456237490", target = 9191
#输出: []
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def backtrack(expr: List[str], i: int, res: int, mul: int):
            if i == n:
                if res == target:
                    ans.append(''.join(expr))
                return
            signIndex = len(expr)
            if i > 0:
                expr.append('')  # 占位，下面填充符号
            val = 0
            for j in range(i, n):  # 枚举截取的数字长度（取多少位）
                if j > i and num[i] == '0':  # 数字可以是单个 0 但不能有前导零
                    break
                val = val * 10 + int(num[j])
                expr.append(num[j])
                if i == 0:  # 表达式开头不能添加符号
                    backtrack(expr, j + 1, val, val)
                else:  # 枚举符号
                    expr[signIndex] = '+'; backtrack(expr, j + 1, res + val, val)
                    expr[signIndex] = '-'; backtrack(expr, j + 1, res - val, -val)
                    expr[signIndex] = '*'; backtrack(expr, j + 1, res - mul + mul * val, mul * val)
            del expr[signIndex:]

        backtrack([], 0, 0, 0)
        return ans

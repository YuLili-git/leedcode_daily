#给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
#如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
#示例 1：
#输入：1
#输出：true
#示例 2：
#输入：10
#输出：false
#示例 3：
#输入：16
#输出：true
#示例 4：
#输入：24
#输出：false
#示例 5：
#输入：46
#输出：true
def countDigits(n: int) -> Tuple[int]:
    cnt = [0] * 10
    while n:
        cnt[n % 10] += 1
        n //= 10
    return tuple(cnt)

powerOf2Digits = {countDigits(1 << i) for i in range(30)}

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return countDigits(n) in powerOf2Digits

#给你一个整数数组 distance 。
#从 X-Y 平面上的点 (0,0) 开始，先向北移动 distance[0] 米，然后向西移动 distance[1] 米，向南移动 distance[2] 米，向东移动 distance[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。
#判断你所经过的路径是否相交。如果相交，返回 true ；否则，返回 false 。
#示例 1：
#输入：distance = [2,1,1,2]
#输出：true
#示例 2：
#输入：distance = [1,2,3,4]
#输出：false
#示例 3：
#输入：distance = [1,1,1,1]
#输出：true
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)

        # 处理第 1 种情况
        i = 0
        while i < n and (i < 2 or distance[i] > distance[i - 2]):
            i += 1

        if i == n:
            return False

        # 处理第 j 次移动的情况
        if ((i == 3 and distance[i] == distance[i - 2])
                or (i >= 4 and distance[i] >= distance[i - 2] - distance[i - 4])):
            distance[i - 1] -= distance[i - 3]
        i += 1

        # 处理第 2 种情况
        while i < n and distance[i] < distance[i - 2]:
            i += 1

        return i != n

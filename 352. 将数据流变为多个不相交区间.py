#给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。
#实现 SummaryRanges 类：
#SummaryRanges() 使用一个空数据流初始化对象。
#void addNum(int val) 向数据流中加入整数 val 。
#int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。
#示例：
#输入：
#["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
#[[], [1], [], [3], [], [7], [], [2], [], [6], []]
#输出：
#[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
#解释：
#SummaryRanges summaryRanges = new SummaryRanges();
#summaryRanges.addNum(1);      // arr = [1]
#summaryRanges.getIntervals(); // 返回 [[1, 1]]
#summaryRanges.addNum(3);      // arr = [1, 3]
#summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
#summaryRanges.addNum(7);      // arr = [1, 3, 7]
#summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
#summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
#summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
#summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
#summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]
from sortedcontainers import SortedDict

class SummaryRanges:

    def __init__(self):
        self.intervals = SortedDict()

    def addNum(self, val: int) -> None:
        intervals_ = self.intervals
        keys_ = self.intervals.keys()
        values_ = self.intervals.values()
        interval1 = intervals_.bisect_right(val)
        if interval1 == 0:
            interval0 = len(intervals_)
        else: 
            interval0 = interval1 - 1

        if interval0 != len(intervals_) and keys_[interval0] <= val <= values_[interval0]:
            return
        else:
            left_aside = (interval0 != len(intervals_) and values_[interval0] + 1 == val)
            right_aside = (interval1 != len(intervals_) and keys_[interval1] - 1 == val)
            if left_aside and right_aside:
                left, right = keys_[interval0], values_[interval1]
                intervals_.popitem(interval1)
                intervals_.popitem(interval0)
                intervals_[left] = right
            elif left_aside:
                intervals_[keys_[interval0]] += 1
            elif right_aside:
                right = values_[interval1]
                intervals_.popitem(interval1)
                intervals_[val] = right
            else:
                intervals_[val] = val

    def getIntervals(self) -> List[List[int]]:
        return list(self.intervals.items())

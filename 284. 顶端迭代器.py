#请你设计一个迭代器，除了支持 hasNext 和 next 操作外，还支持 peek 操作。
#实现 PeekingIterator 类：
#PeekingIterator(int[] nums) 使用指定整数数组 nums 初始化迭代器。
#int next() 返回数组中的下一个元素，并将指针移动到下个元素处。
#bool hasNext() 如果数组中存在下一个元素，返回 true ；否则，返回 false 。
#int peek() 返回数组中的下一个元素，但 不 移动指针。
#示例：
#输入：
#["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
#[[[1, 2, 3]], [], [], [], [], []]
#输出：
#[null, 1, 2, 2, 3, false]
#解释：
#PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
#peekingIterator.next();    // 返回 1 ，指针移动到下一个元素 [1,2,3]
#peekingIterator.peek();    // 返回 2 ，指针未发生移动 [1,2,3]
#peekingIterator.next();    // 返回 2 ，指针移动到下一个元素 [1,2,3]
#peekingIterator.next();    // 返回 3 ，指针移动到下一个元素 [1,2,3]
#peekingIterator.hasNext(); // 返回 False
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.array = []
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.array:
            return self.array[-1]
        else:
            self.array.append(self.iterator.next())
        return self.array[-1]        
        

    def next(self):
        """
        :rtype: int
        """
        if self.array:
            return self.array.pop()
        else:
            return self.iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.array:
            return True 
        return self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

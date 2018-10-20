# Stack with O(1) minimum value retrieval, but uses twice the space/memory
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        # Stack of pairs [0] - value, [1] - curMin at time of this value
        self.stack = []
        curMin = None
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin is None or x < curMin:
            curMin = x
            
        self.stack.append([x, curMin])
        
    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            return self.stack.pop()[0]
        return None
        
    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]
        return None
        
    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

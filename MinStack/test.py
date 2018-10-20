from MinStack import MinStack
minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print(minStack.getMin());  # --> Returns -3.
minStack.pop();
print(minStack.top());     # --> Returns 0.
print(minStack.getMin());  # --> Returns -2.

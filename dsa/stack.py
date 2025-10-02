# Stack
# Last in First Out Structure

# Python implements this functionality with lists
stack = []

# Add to the top of the stack: O(1)
stack.append(1)

# View the element on the top of the stack: O(1)
top = stack[-1]

# Pop the top element (remove and return): O(1)
x = stack.pop()

# Size and isEmpty: O(1)
size = len(stack)
empty = size == 0


# Algorithms for stacks
# DFS traversal and backtracking
# Expression Evaluation
# Monotonic Stacks can be used to solve next greatest/smallest problems (by maintining the monotonic property)


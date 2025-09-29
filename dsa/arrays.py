# Array
# Python list type implements both Fixed and Dynamic Arrays

# initialize - for a fixed size, multiplication is the most efficient
# list comprehensions are slower but more flexible for initialization
# using the list() function - it can take any iterable
lst = []
lst2 = [0]*100
lst3 = [x for x in range(10)]
lst4 = list(range(10))

# Array ADT Operations
# Access by index: O(1)
x = lst2[25]

# Update by index: O(1)
lst2[25] = 1

# Append: amoritized O(1) - if capacity is exceeded, a copy into larger size is needed: O(n)
lst.append("only amoritized O(1)")

# Delete by index: O(n) due to resizing
del lst2[25]

# Insert at position: O(n) due to resizing / copy over
lst2.insert(0, 1234)

# Length of list: O(1)
len(lst)

# Slicing: O(k) where k is the slice size
# slices will always allocate additional space, and produce a shallow copy

# Shallow copies include the same references
# Modifying the contents of those references (anything that is mutable), will also appear in the copy
# However, modifying the structure (add/remove, etc) will not change the copy (the copy has it's own references)

# Example: int is immutable, the newlst will not be changed
newlst = lst3[:5]
lst3[0] = 12345
# print(newlst, lst3)

# Example: lists are mutable, modifying the original will affect the copy 
original = [[1, 2], [3, 4]]
slice_copy = original[:]  # Shallow copy: [[1, 2], [3, 4]]
original[0][0] = 99  # Modify the nested list
# print(original)    # [[99, 2], [3, 4]]
# print(slice_copy)  # [[99, 2], [3, 4]] (changed!)


# Python STL functions for common list operations 

# Extending a list from an iterable
lst.extend(range(10))

# List concat O(m + n) will be copied (shallow) into a new list
concat = lst + lst2

# remove all items in a list: O(n)
# similar to del a[:]
lst.clear()

# Pop: remove and return from index
# O(n), for each element after i, it must be copied over
# so pop(0) is n, while pop() is O(1), default is end of the list
removed = lst2.pop(4)

# Remove element: O(n)
# removes the first item that is equal to x, always returns None 
lst2.remove(0)

# Frequency of x: O(n)
# Get the count of how many times the element x occurs in the list
c = lst2.count(0)

# Reverse a list in place: O(n)
lst.reverse()

# Sort a list in place: O(nlogn)
lst.sort()

# Or use sorted() to get an interator for the elements
newsorted = sorted(lst)

# Zip function - takes any number of iterables and "zips" them together into elementwise tuples
# for example combine x and y coordinates into an interable of tuples
# Note that it will combine elements up to the shortest iterator (for longest, use zip_longest from intertools)
# In general zip is faster (implemented in C) than traditional traversals
xs = [0, 1, 2, 3, 4]
ys = [0, 1, 4, 9, 16]
points = list(zip(xs, ys))
# print(points)

# Example usage to transpose a matrix
matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

# in this case, the matrix is a collection of iterables, * is used to unpack all of them
transposed = list(zip(*matrix))
# print(transposed)

t2 = [list(row) for row in list(zip(*matrix))]
# print(t2)

















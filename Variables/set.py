#collection of unique elements
#doesn't care which order you created it will auto ordered using hash-no sorted values
s = {1,8,5,7,11,57,85,2,400,8}
print(s)
a = {1,1,2,2,5,7,4,8,9,44,55,66,85,55,22,10}
print(a)
#Remove () will remove particular value from set
a.remove(22)
print(a)
#copy() will create a copy of a set
new_set = s.copy()
print(new_set)
#add method will add new element to the set
new_set.add(10)
print(new_set)
#pop() will remove last in element from set
s.pop()
print(s)
#s[1] #set doesn't support sequence
print('A U S : ',a.union(s))
A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}

# Equivalent to A-B
print(A.difference(B))

# Equivalent to B-A
print(B.difference(A))

A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}

result = A.difference_update(B)
#result will be None
#A will be equal to A - B
#B will be unchanged
print('A = ', A)
print('B = ', B)
print('result = ', result)
#The discard() method removes a specified element from the set (if present).
numbers = {2, 3, 4, 5}

numbers.discard(3)
print('numbers = ', numbers)

numbers.discard(10)
print('numbers = ', numbers)
#The intersection() method returns a new set with elements that are common to all sets.
A = {2, 3, 5}
B = {1, 3, 5}

# compute intersection between A and B
print(A.intersection(B))

#The isdisjoint() method returns True if two sets are disjoint sets. If not, it returns False.

A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))
print('Are B and C disjoint?', B.isdisjoint(C))

#The issubset() method returns True if all elements of a set are present in another set (passed as an argument).
# If not, it returns False.
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

# Returns True
print(A.issubset(B))

# Returns False
# B is not subset of A
print(B.issubset(A))

# Returns False
print(A.issubset(C))

# Returns True
print(C.issubset(B))
#The Python set update() method updates the set, adding items from other iterables.
A = {'a', 'b'}
B = {1, 2, 3}

result = A.update(B)

print('A =', A)
print('result =', result)
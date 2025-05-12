# sets is an unordered collection of unique elements.
# Sets are mutable
#automatically arranges in ascending order.

my_set={1,2,3,4,5}
my_set.add(6)
my_set.add(0)
my_set.remove(6)
my_set.discard(0)
# my_set.remove(7) gives error if it doesnt find any element to discard
# my_set.discard(7) give set as it is if it doesnt find any element to discard

print(my_set)

#sets operations

set1={1,2,3,4}
set2={3,4,5,6}

#union
print(set1 | set2) #outputs {1,2,3,4,5,6}

#intersection
print(set1 & set2) #outputs {3,4}

#difference 
print(set1-set2) #outputs {1,2}
print(set2-set1) #outputs {5,6}

#symmetric difference
print(set1 ^ set2) #outputs {1,2,5,6}


#alternate way
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

#frozen sets: frozen sets are immutable
fs=frozenset({1,2,3,4,5})
print(fs)









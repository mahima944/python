
myset={1,2,3}
frozenset=frozenset(myset)
print(myset)
print(frozenset)

#set operations
s1={1,2,3,4}
s2={1,3,4,8}
print("union of sets ",s1 | s2)
print("intersectoin of sets ",s1 & s2)
print("difference of sets is ",s1-s2)
print(" symmetric difference of sets is ",s1 ^ s2)

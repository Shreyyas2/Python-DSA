#Sets - InBuilt Datatypes in Python
'''1)it removes all the dublicate elements by default
   2)it is unordered, it does not follow any specific order'''

#defining a set
my_set={1,2,3}
print(type(my_set))

#adding an element to a set
my_set2={1,2,3}
print(my_set2.add(4))

#adding an already existing element to a set (duplicate so, it will ignore)
my_set3={1,2,3,4}
after_adding=my_set3.add(4)
print(after_adding)

#deleting an element from a set
my_set4={1,2,3}
my_set4.remove(3)
print(my_set4)

#now if we delete an element, which originally does not exist, an error will show up


#now to remove an element which originally does not exist, without any error
my_set5={1,2,3,4}
my_set.discard(5)
print(my_set5) #".discard" can also be used to remove an already existing element

#pop method
my_set6={1,2,3}
removed_element=my_set6.pop()
print(removed_element)
print(my_set6)

#clear method - to remove each elements from a set
my_set7={1,2,3}
cleared=my_set7.clear()
print(cleared)

#set membership test- it basicslly checks if any specific element is present in a set and returns in true/false
my_set8={1,2,3,4}
print(3 in my_set8)
print(8 in my_set8)

#mathematical operations
#union- it basically merges two sets and also removes dublicate elements
my_set9={1,2,3,4,5}
my_set10={5,6,7}
union_set=my_set9.union(my_set10)
print(union_set)

#to get common elements from two sets
my_set11={1,2,3}
my_set12={2,3,4}
intersection_set=my_set11.intersection(my_set12)
print(intersection_set)

#To update any set after intersection
my_set11.intersection_update(my_set12)
print(my_set11)

#difference- it returns unique elements between two sets
my_set13={1,2,3}
my_set14={3,4,5}
print(my_set13.difference(my_set14))
print(my_set14.difference(my_set13))

#to get combined unique elements from two sets
print(my_set13.symmetric_difference(my_set14))

#subset & superset
my_set15={1,2,3}
my_set16={3,4,5}
print(my_set15.issubset(my_set16))
print(my_set15.issuperset(my_set16))

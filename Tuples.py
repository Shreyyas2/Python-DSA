#Tuples : It is an ordered collections of items that are immutable

#Creating a tuple
empty_tuple=()
print(empty_tuple)
print(type(empty_tuple))

mixed_tuple=(1,'shreyas',3.14,True)
print(mixed_tuple)

#Conversion of list to tuple
number=tuple([1,2,3])
print(number)
print(type(number))

#Conversion of tuple to list
number2=list((1,2,3))
print(number2)
print(type(number2))

#Accessing tuple elements
print(mixed_tuple[0]) #syntax: print(variable_name[index])
print(mixed_tuple[1])
print(mixed_tuple[2])
print(mixed_tuple[3])

#Slicing is same as list

#Tuple operations
#1) adding of two tuples
tup1=(1,2,3)
tup2=('shreyas',4)
concatenation_tuple=tup1+tup2
print(concatenation_tuple)

#tuples are immutable
#tup1[1]='shreyas'
#print(tup1) #error will be occured

#Tuple Methods
tup3=(1,2,2,3,3,3,4,4,4,4)
print(tup3.count(1))
print(tup3.count(2))
print(tup3.count(3))
print(tup3.count(4))

#Unpacking and Packing of a tuple
#1)Packing
packed_tuple=1,'hello',2
print(packed_tuple)

#2)Unpacking
a,b,c=packed_tuple
print(a)
print(b)
print(c)

#Unpacking with *
#tup4=(1,2,3,4)
#tup4=first,*middle,last
#print(first)
#print(middle)
#print(last)

#Nested list and tuple
lst=[[1,2],[3,4,5]]
print(lst[0][1]) #first index will return [1,2] and the other index will act as subindex for the same indexed lst

tup5=((1,2,3),('a','b'))
print(tup5[0][2])



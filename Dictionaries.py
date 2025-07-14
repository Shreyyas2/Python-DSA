#Dictionaries - unordered collection of items, they store data in key-value pair, where key is immutable and values are mutable

#Creating Dictionaries
empty_dict={}
print(empty_dict)
print(type(empty_dict))

student={'name':'krishna','age':20,'course':'BCA'}
print(student)

#Accessing each element by their keys
print(student['name'])
print(student['age'])
print(student['course'])

#Another Method of accessing elements
print(student.get('name'))
print(student.get('age'))
print(student.get('last_name')) #Here 'last_name' is not defined, so it will return 'NONE'

#If you are printing a key which does not originally exists, and dont want 'NONE' in return then,
print(student.get('last_name','Not Available')) #Here it will return 'Not Available' instead of 'NONE', you can give any user specific statement

#Modifying dictionaries elements
student['age']=21
print(student) #Age will get updated

student['address']='India'
print(student) #Adding a new element

#Deleting an element
#deleting_element=del_student['course']
#print(deleting_element)

#Dictionaries Methods
keys=student.keys()
print(keys) #To get all the keys

value=student.values() 
print(value) #To get all the values

items=student.items()
print(items) #To get all key-value pairs

#Shallow copy
#Here a copy of original dictionary gets created but in different memory location, so if the original dictionary gets modified, the copied verion does'nt get affected
student_copy=student.copy()
print(student_copy)
student['age']=22
print(student)
print(student_copy)

#Iterating over a dictionary
#1) keys
for keys in student.keys():
    print(keys)
#2) values
for values in student.values():
    print(values)
#3) both keys&values
for keys,values in student.items():
    print(f'{keys}:{values}')

#Dictionary Comprehension
squares={x:x**2 for x in range(10)}
print(squares)

#For even squares
even_squares={x:x**2 for x in range(10) if x%2==0}
print(even_squares)

#Merging of two dictionaries
dict1={'a':1,"b":2}
dict2={'b':3,'c':4}
merged_dict={**dict1,**dict2}
print(merged_dict) #It will merge two dictionaries, and as here 'b' is present in both the dictionaries, it will return the most recent value of 'b' or any variable if repeated so. 
    




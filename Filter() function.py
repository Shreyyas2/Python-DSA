#filter() - it is used to filter out items from a list based in a condition

def even(num):
    if num%2==0:
        return True
e=even(12)
print(e)

lst=[1,2,3,4]
l=list(filter(even,lst))
print(l) #here, the filter() , filtered the odd numbers from the lst and returned only even

#filter w lambda function
numbers=[1,2,3,4]
lst=list(filter(lambda x:x>2, numbers))
print(lst)

#filter w lambda function and multiple conditons
numbers1=[1,2,3,4,5,6,7,8]
lst=list(filter(lambda x:x>4 and x%2==0, numbers1))
print(lst)

#filter() w dictionaries

people=[
    {'name':'shreyas','age':20},
    {'name':'krishna','age':21},
    {'name':'shreyas','age':22}]
def age(people):
    return people['age']<22
l1=list(filter(age,people))
print(l1)
    

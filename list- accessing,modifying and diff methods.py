#list: accessing,modifying and diff methods
list=[1,'shreyas',True]
print(list)#it can hold every type of data

#accessing list elements through indexing
fruits=['apple','banana','guava','watermelon']
print(fruits[2])
print(fruits[1:3])
print(fruits[-1])

#modifying list elements
fruits=['apple','banana','guava','watermelon']
fruits[1]='kiwi'
print(fruits)
fruits.append('orange')
print(fruits)
fruits.extend('big orange')
print(fruits)
fruits.remove('watermelon')
print(fruits)
fruits.insert(2,'small kiwi')
print(fruits)
fruits.pop()
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.clear()
print(fruits)

#map()- it is particularly useful for transforming data in a list comprehensively

num1=[1,2,3]
num2=[4,5,6]
add_num=list(map(lambda a,b:a+b, num1,num2))
print(add_num) #syntax- list(map(lambds x:y,x+y ,lst1,lst2)) any operations can be performed

#map() to convert list of strings to integers
str=('1','2','3')
int_conversion=list(map(int,str))
print(int_conversion) #'int' is an inbuilt function to convert any datatype to integer


#map() to capatilise
#words=('apple','banana')
#upper_word=list(map(str.upper,words))
#print(upper_word)

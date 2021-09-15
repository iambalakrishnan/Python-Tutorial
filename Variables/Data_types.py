#Numeric data types has four major data types
#int
num = 2
print(type(num))
#float
var = 5.5
print(type(var))
#complex
com = 2 + 5j
print(type(com))
#bool
bol = True
print(type(bol))
#converting a data type to another using constructor
b = int(var) #int constructor will convert copatable numeric values to integer
print('value of b is : ',b,' type of b is ', type(b))
#Lets converrt int into float
k = float(num)
print('value of k is : ',k,' type of k is ', type(k))
#complex parameter
c = complex(b,k)
print('c : ',c,' type : ',type(c))
#when you don't pass 2nd variable it will be considered as 0
c1 = complex(b)
print('c1 : ',c1,' type : ',type(c1))
#bool data type
m = True
n = False
print(type(m), type(n))
print(int(m), int(n))

#Sequence
#list
#set
#tuple
#string
#range
lst = [1,2,5,'hello',True]
print(lst,type(lst))
s = ('a',2,3,True)
print(s,type(s))
tup = {'a','a',1,2,2,3,3,5,True,True}
print(tup,type(tup))

st = "Hello world"
print(st,type(st))

#range will create a range of values
print(range(10))
print(list(range(10)))#converting range into list to print the element
#range iteration with iterate value
print(list(range(0,10,2))) #0- starting value, 10-limit, 2-step value
print(type(range(10)))

#Dictionary
#keys should be unique in dictionary and values can be repeated
d = {'iphone' : 'apple', 'android':['google','samsung','nokia','oppo','huawei','redmi'], 'windows' : ['microsoft','nokia']}
print(d, type(d))
print(d.keys())
print(d.values())
print(d['android'])
print(d['iphone'])
print(d['windows'])
print(d.get('iphone'))
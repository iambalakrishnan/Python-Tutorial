#for loop

for i in range(10):#start value = 0, end=10, increment by 1
    print(i)
print()

#we can also mention starting poiint, end point and increment value as well
for i in range(5, 100,5):
    print(i)
print()

#we can also use decrement
for i in range(50, 0,-5):#-5 because it will always goes in ascending order
    print(i)
print("####"*10)

for i in range(1,21):#auto increment by 1
    if i % 5!=0:#print only if number is not divisible by 5
        print(i)
print("####"*10)
#print values in list
x = ['hello', 10, 2.5, 'python', True]
for i in range(len(x)):
    print(x[i]) #index access

print()

for i in x:
    print(i)#element access

string = "Hello world"
for i in string:
    print(i) #access using elements
print()
#we can have list in the for loop itself
for i in [1,1.5,'python']:
    print(i)

#finding id of a variable
num = 10
print(id(10))
name = "Bill"
print(id(name))
a=10
b=a
print('Address of a : ',id(a))
print('Address of b : ',id(b))
a=15
print('value if a is ',a,'\naddress of a ',id(a))
print('value if b is ',b,'\naddress of a ',id(b))
a=20
b=a
print('value if a is ',a,'\naddress of a ',id(a))
print('value if b is ',b,'\naddress of a ',id(b))
a=a+5
print('value if a is ',a,'\naddress of a ',id(a))
print('value if b is ',b,'\naddress of a ',id(b))
k=25
print('value if k is ',k,'\naddress of a ',id(k))
c=1.5
print(type(c))

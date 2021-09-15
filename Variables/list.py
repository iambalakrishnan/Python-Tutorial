nums = [10,25,12,18,28,30]
print(nums)
#finding type of variable
print(type(nums))

print(nums[0])
print(nums[5])
print(nums[-1])
print(nums[0:3])
#print(nums[0:2,4:5])
#print(nums[0,2])
print(nums[3:])

names = ['elon','musk','jobs','pichai']
print(names)

values = [10, 10.5, 'pichai',True]
print(values[-1])
#boolean true is euqals to 1
print(values[-1]==1)
#We can assign any number of list variables to new list
mil = [names,values]
print(mil)
#sorting a list
nums.sort()
print(nums)
print(sorted(names))

names.remove('musk')
print(names)
#copying a new list
new_list = names.copy()
print(new_list)
#append will add values at last
names.append('bill')
print(names,new_list)
#insert requires index values
names.insert(-1,'moroney')
print(names)
#removing particualr value
names.remove('moroney')
print(names)
#reverseing the order of values in list
names.reverse()
print(names)
print(len(names))

#extending list with multiple vales
nums.extend([11,31,32,11,12,10,15])
print(nums)
print(nums.count(10))
#finding index of particular value
print('index of  ',nums[nums.index(15)],' is : ',nums.index(15))
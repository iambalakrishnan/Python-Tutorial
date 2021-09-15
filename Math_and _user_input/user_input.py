#user input
x = int(input("Enter value for x : ")) #input will always give you str format
y = int(input("Enter value for y : "))#so need to type cast into integer type
z = x + y
print(f" x + y = {z}")

#take input from user in char format
ch = input('enter a char')
print(ch)
#what if a user enter multiple characters
ch = input('enter a char')
print(ch[0])
#while getting user input we can expect number of characters using input function
#input will fetch entire string and it will assign only number of strings to ch variable
ch = input('enter a char')[2]
print(ch)
#bunch of char as well
ch = input('enter a char')[0:3]
print(ch)

#eval function will evaluate expresssion
result = eval(input("Enter expression : "))
print(result)
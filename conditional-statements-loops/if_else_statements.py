#if elif else

x=2
if x%2==0:
    print("even number")
    if x > 5:#nested if
        print('x is greater than 5')
    elif x > 3: #elif condition check
        print('x is greater than 3 but less than 5')
    elif x==2:
        print(f'x is less than 3 and x is : {x}')

else:
    print("odd number")
print("Bye")


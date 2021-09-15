#prime number is a number which is only divisible by itself

num = int(input("Enter the number : "))
for i in range(2,num):
    if num % i == 0:
        print(f"{num} is Not prime")
        break
else:
    print(f" {num} is prime number")

num = 12
if num > 1:
    for i in range(2, num//2):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

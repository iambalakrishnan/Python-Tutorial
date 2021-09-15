#printing patterns
# # # #
# # # #
# # # #
for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()
#
# #
# # #
print()
for i in range(4):
    for j in range(i+1):
        print("# ", end="")
    print()
# # # #
# # #
# #
#
print()
for i in range(4):
    for j in range(4-i):
        print("# ", end="")
    print()

print()
for i in range(1,5):
    for j in range(1,5-i):
        print(j, end="")
    print()


str1='ABCD'
str2='PQR'
for i in range(4):
     print(str1[ : i+1 ] + str2[ i : ])
print()

for i in range(4):
    for j in range(4 - i):
        print(i + j + 1, end=' ')

    print()

rows = int(input("Enter the number of rows: "))
for i in range(1, rows):
    for j in range(1, i + 1):
        # It prints multiplication or row and column
        print(i * j, end='  ')
    print()
#continue
for i in range(1,101):

    if i % 3 == 0 or i%5==0:
        continue#skip the current loop operation and goes for next iteration
    print(i)
print("Bye")
print()
#Pass
for i in range(1,50):
    if i%2==0:
        pass
    else:
        print(i)
print("Bye")

#continue - will skip current loop operation and continue to next iteration
#pass will pass statements
def fun():
    pass


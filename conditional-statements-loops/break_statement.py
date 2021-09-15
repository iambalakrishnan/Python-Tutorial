#break statement
avc = 6
x = int(input("Enter no of candy : "))
i=1
if x>avc:
    print(f"we don't have requested no of candy, we have only {avc} candy")
    ip = input("Do you want to proceed y/n ")
    if ip=='y':
        while i <= x:
            if i>avc:
                print(f"We don't remaining {x-avc} candy ")
                break
            print("candy")
            i+=1
    else :
        print("Bye")
else:
    while i <= x:
        print("candy")
        i += 1
print("Bye")

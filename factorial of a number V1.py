# program to find factorial of a number V1
num=int(input("enter num to find factorial > 0 : "))
fact=1
if num>0:
    for i in range(num):
        fact= fact*(i+1)
    print(f"factorial of {num} is {fact}")

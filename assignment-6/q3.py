#check if power of 2

num = int(input("Enter a number: "))

if num & num-1 == 0:
    print("The number is a power of 2")
else:
    print("The number is not a power of 2")

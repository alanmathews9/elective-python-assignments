# 11. Check if the items in the list are sorted in ascending or descending order and print suitable messages
# accordingly. Otherwise, print “Items in list are not sorted”
l=list()
n=int(input("Enter the number of elements in list: "))
for i in range(n):
    num=int(input("no:"))
    l.append(num)
print(f'list is {l}')
if l == sorted(l):
    print("Items in list are sorted in ascending order.")
elif l == sorted(l, reverse=True):
    print("Items in list are sorted in descending order.")
else:
    print("Items in list are not sorted.")

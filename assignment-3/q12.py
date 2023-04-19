# 12.Remove all duplicate elements from a list i/p: 10 20 20 30 40 o/p: 10 30 40
l=[]
n=int(input("Enter the elements of the list: "))
for i in range(n):
    num=int(input("no:"))
    l.append(num)
print(f'list l is: {l}')
s=set(l)
print(f'After removing duplicates in l: {list(s)}')
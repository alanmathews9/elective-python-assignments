# 13.Find the number with largest frequency of occurrence. i/p: 10 20 30 40 40 40 50 50 o/p: 40
# (Note: there may be more than one element)
l=[]
n=int(input("Enter the elements of the list: "))
for i in range(n):
    num=int(input("no:"))
    l.append(num)
print(f'list l is: {l}')
s=set(l)
max=0
for num in s:
    if l.count(num)>=max:
     max=l.count(num)
largest=[]
for num in s:
   if l.count(num)==max:
      largest.append(num)
print(f'No:(s) with largest occurrence: {largest} with frequency {max}')
# 3. Read list of students names and do the following
# a) Sort the name in alphabetical order
# b) Find the name with largest length
# c)print the names starting with letter ‘A’ (assume first letter capital)
# d) Print the names in reverse alphabetical order with all names converted to capital letters.
# e) Print the names in the order of length

names=[]
n=int(input("Enter the number of students: "))
for i in range(n):
    name=input("Name: ")
    names.append(name)
  
print(f'\nBefore sorting : {names}')
names.sort()
print(f'After sorting : {names}')

names.sort(key=len,reverse=True)
length=len(names[0])#more than one name with same largest length
longest=""
for name in names:
    if len(name)==length:
        longest+=name+" "
print(f'longest name(s): {longest}')
print(f'names in the desc order of length: {names}')

flag=0
print(f'Number of students name starting with A:',end=" ")
for name in names:
    if name[0]=='A':
        flag=1
        print(f'{name}',end=" ")

if flag==0:
    print(f'--\n')



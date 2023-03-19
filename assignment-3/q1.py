# 1. Write commands for the following
# a. Create an empty list(stud)
# b. Add your roll number to the list(use + operator)
# c. Append your name(use append)
# d. Extend the list with your place and pin and mobile number(extend)
# e. Insert your KTU-ID at stud[0]
# f. Print your KTU-ID and name
# g. Print the number of characters in your name.
# h. Print last 5 digit of the phone number
# I.Reverse the stud list
# j.Find the index of your name.

stud=[]
print(f'stud initially: {stud}')
rollno=[64]
stud=stud+rollno
stud.append("Alan")
details=["Kochi","682021","9712342102"]
stud.extend(details)
stud.insert(0,"MDL20CS115")
print("KTUid: ",stud[0]," name: ",stud[2]) 
print(f'number of characters in name: {len(stud[2])}')
print(f'last 4 digits of phone number: {stud[5][-5:]}')
print(f'reversed list is:{stud[::-1]}')
print(f'index of name: {stud.index("Alan")}')
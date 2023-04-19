# 4. Use list comprehension to create lists
# a)powers of 3 upto 20
# b) Numbers less than 100 which are divisible by 3

list_multiple=[x for x in range(100) if x%3==0]
print(f'list of numbers<100 and divisible by 3:\n{list_multiple}')
list_powers=[3**x for x in range(21)]
print(f'powers of 3 upto 3^20:\n{list_powers}')

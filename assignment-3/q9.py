# 9.Read list of numbers and find the mean, median and standard deviation.
import math
numbers = input("Enter a list of numbers, separated by spaces: ")
numbers = numbers.split()
numbers = [float(num) for num in numbers]
mean = sum(numbers) / len(numbers)
numbers.sort()
if len(numbers) % 2 == 0:
    median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
else:
    median = numbers[len(numbers)//2]
std_dev = math.sqrt(sum([(num - mean)**2 for num in numbers]) / len(numbers))
print("Mean =", mean)
print("Median =", median)
print("Standard deviation =", std_dev)

"""

Smallest Multiple - Problem 5

2520 is the smallest number that can be divided by each of the numbers from to without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 
to 20 ?

"""

def greatest_common_div(a,b): return b and greatest_common_div(b, a % b) or b
def least_common_div(a,b): return a * b / greatest_common_div(a,b)

number = 1
for index in range(1, 31):
     number = least_common_div(number, index)
print(number)
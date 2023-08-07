#Find the sum of multiples of 3 or 5 below 1000:

# Initialize sum
sum = 0
# Create a for loop to iterate through numbers up to 1000.
# Write a condition to test if a number is a multiple of 3 or 5. If true, add the number to the sum.

for number in range(1000):
    if number % 3 == 0 or number % 5 == 0:
        sum += number
# Print the sum.
print(sum)

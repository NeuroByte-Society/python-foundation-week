# Take input from user: the number up to which the sum is to be calculated
n = int(input("Enter the value of n: "))

# Initialize the total sum to 0
total = 0

# Loop from 1 to n (inclusive)
for i in range(1, n + 1):
    # Add the current number 'i' to the total sum
    total += i

# After the loop, print the final sum
print(f"Sum from 1 to {n} is: {total}")

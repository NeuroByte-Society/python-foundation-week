# Take an integer input from the user for which to print the multiplication table
num = int(input("Enter a number: "))

# Loop from 1 to 10 (inclusive)
for i in range(1, 11):
    # Print the multiplication result in formatted style
    # e.g., 5 x 3 = 15
    print(f"{num} x {i} = {num * i}")

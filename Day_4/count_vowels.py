# Ask the user to type a sentence
sentence = input("Enter a sentence: ")

# This string contains all vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Start with 0 vowels
count = 0

# Loop through each character in the sentence
for char in sentence:
    # Check if the character is a vowel
    if char in vowels:
        # If it's a vowel, increase the count by 1
        count += 1

# Print the total number of vowels
print(f"Number of vowels: {count}")

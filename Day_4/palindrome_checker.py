# Ask the user to enter some text (word or sentence)
text = input("Enter text: ")

# Convert the text to lowercase and remove all spaces
# This helps us check the text in a simple, uniform way (ignoring case and spaces)
cleaned = text.lower().replace(" ", "")

# Check if the cleaned text is the same when reversed
# cleaned[::-1] means "reverse the string"
if cleaned == cleaned[::-1]:
    # If the text is the same forwards and backwards, it's a palindrome
    print("It's a palindrome!")
else:
    # If it's not the same, it's not a palindrome
    print("Not a palindrome.")

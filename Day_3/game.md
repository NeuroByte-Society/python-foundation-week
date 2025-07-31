# 🛠️ Mini Project: Number Guessing Game

## 🎯 Objective:

Build a simple number guessing game using loops.

## 💡 Features:

* Random number between 1 and 100
* User has limited chances to guess
* Give hints: "Too high" or "Too low"
* End when guessed or attempts exhausted

```python
import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("🎮 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("🔼 Too low!")
    else:
        print("🔽 Too high!")

    print(f"Attempts left: {max_attempts - attempts}")

else:
    print(f"😞 Sorry, you've used all your attempts. The number was {secret_number}.")
```

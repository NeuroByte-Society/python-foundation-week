## 🧠 Mini Task 2: Quiz Dictionary

### Code:

```python
quiz = {
    "What is the capital of France?": "Paris",
    "2 + 2 equals?": "4",
    "Python is dynamically typed? (Yes/No)": "Yes"
}

# Asking questions
score = 0
for question, correct_answer in quiz.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == correct_answer.lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {correct_answer}")

print(f"\nYour score: {score}/{len(quiz)}")

```

### Explanation:

-   Each question is a dictionary key and the answer is the value.
    
-   `.strip().lower()` ensures case-insensitive comparison.
    
-   Simple quiz scoring logic is added.

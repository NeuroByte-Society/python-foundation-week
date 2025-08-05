### 🔹 3. File Reader + Word Counter


def count_words(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            words = text.split()
            print(f"📄 {filename} has {len(words)} words.")
    except FileNotFoundError:
        print("❌ File not found.")

# Example
filename = input("Enter filename (e.g. notes.txt): ")
count_words(filename)

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' ({self.pages} pages)"

    def __len__(self):
        return self.pages

b = Book("Clean Code", 464)
print(b)        # 'Clean Code' (464 pages)
print(len(b))   # 464

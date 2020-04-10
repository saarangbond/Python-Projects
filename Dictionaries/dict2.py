books = {"Poetry":"Dickens", "Ballard":"Mallard", "Evolution":"Dickens"}

for i in books:
    print(i, books[i])
    
print()

print(books)
print()
del books["Poetry"]
print(books)

print()

print(books.pop("Ballard"))
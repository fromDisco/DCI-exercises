f = open("book.txt", "w")

numbers = ""
for i in range(1000000):
    f.write(f"{i}\n")

f.close()

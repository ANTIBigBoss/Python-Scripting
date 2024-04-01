try:
    with open('words.txt', 'r') as file:
        content = file.read()
        words = content.split()
        long_words = [word for word in words if len(word) >= 4]
        print(long_words)

except FileNotFoundError:
    print("File not found!")

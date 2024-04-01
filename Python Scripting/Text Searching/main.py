# Function named "histogram" with logic
def histogram(word):
    d = dict()
    for letter in word:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    print(d)

try:
    # Just kept it in the same directory as the python file so that it'd work on your device too seamlessly
    f = open('CORRECT.txt', 'r')
    word = f.read()
    f.close()
    print("Histogram of the work CORRECT is:")
    # Call the histogram function and pass it the word variable
    histogram(word)
    # Putting this new line here to show that this works and the exception works
    print("\n")

except:
    print("Error: File name CORRECT.txt not found.")

    # Putting this second try here to show that this works and the exception works
try:
    # Just kept it in the same directory as the python file so it'd work on your device as well seamlessly
    f = open('CORRECT1.txt', 'r')
    word = f.read()
    f.close()
    histogram(word)

except:
    print("Error: File name CORRECT1.txt not found.")
    quit()
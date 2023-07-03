word = input()

try:
    word = int(word)
    print(word)
except ValueError:
    print("Please input a number")
    exit()

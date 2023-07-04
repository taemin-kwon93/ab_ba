a = input()
b = input()

try:
    a = int(a)
    b = int(b)
    print(a)
    print(b)
except ValueError:
    print("a or b is not int")

two_digit_number = input("Type a two digit number: ")
# Type a two digit number: 30

print(type(two_digit_number)) # <class 'str'>
print(type(int(two_digit_number))) # <class 'int'>

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
print(type(first_digit)) # <class 'str'>
print(second_digit) # 0

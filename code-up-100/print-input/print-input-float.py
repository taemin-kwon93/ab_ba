number = input()

try:
    cast_number_to_float = float(number)
    print(cast_number_to_float)
except ValueError:
    print("input value is not number")

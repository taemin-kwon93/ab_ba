number = input()
iteration_count = 3

try:
    cast_number_to_float = float(number)
    for i in range(iteration_count):
        print(cast_number_to_float)

except ValueError:
    print("ValueError")

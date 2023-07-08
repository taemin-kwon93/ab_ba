x, y = input().split()


def main(first_number, second_number) -> int:
    try:
        int_x = int(first_number)
        int_y = int(second_number)
        result = int_x - int_y
        return result
    except ValueError:
        return None


minus_result = main(x, y)

if minus_result is not None:
    print(minus_result)
else:
    print('input value is not integer')

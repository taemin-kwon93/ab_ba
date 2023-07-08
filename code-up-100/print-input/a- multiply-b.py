x, y = input().split()


def main(a, b) -> int:
    try:
        float_a, float_b = cast_to_float(a, b)
        return multiply(float_a, float_b)
    except ValueError:
        return None


def cast_to_float(first_value, second_value) -> float:
    try:
        float_x = float(first_value)
        float_y = float(second_value)
        return float_x, float_y
    except ValueError:
        return None


def multiply(first_value, second_value) -> float:
    return first_value * second_value


print(main(x, y))
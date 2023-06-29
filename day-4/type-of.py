# some string variables here
name: str = "test"
age: int = 30

# print the type of the variables
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>

name = 31
print(type(name))  # <class 'int'>

age = name
print(age)
print(name)

name = 32
print(age)
print(name)

# is 연산자는 두 변수가 같은 객체를 참조하는지 확인하는 연산자입니다. first_list와 second_list는 같은 값을 가지는 두 개의 리스트이므로,
# == 연산자로 비교하면 True가 나오지만, is 연산자로는 두 변수가 서로 다른 객체를 참조하기 때문에 False가 나옵니다.
# 즉, == 연산자는 두 값이 동일한지 비교하고, is 연산자는 두 변수가 동일한 객체를 참조하는지 비교합니다.
first_list = [1, 2, 3]
second_list = [1, 2, 3]
third_list = first_list

print(first_list == second_list)  # True
print(first_list is second_list)  # False
print(first_list is third_list)  # True

first_list = [2, 3, 4]
print(first_list)  # [2, 3, 4]
print(third_list)  # [1, 2, 3]

third_list = first_list
first_list[0] = 5
print(first_list)  # [5, 3, 4]
print(third_list)  # [5, 3, 4]

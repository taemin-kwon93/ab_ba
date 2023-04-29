print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
num_persons = input("How many people to split the bill? ")
print('total_bill: ', total_bill, '\nnum_persons: ', num_persons)
divide_bill = float(total_bill) / int(num_persons)
print('divide_bill:', divide_bill)
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip = divide_bill * (int(tip_percentage) / 100)

print(tip)
# 소수 둘 째 자리까지 계산하여 출력
tip2 = round(tip, 2)
print(tip2)

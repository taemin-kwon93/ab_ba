# 총 6개의 글자를 input()으로 입력받고 두 글자씩 나누어 year, month, day에 저장한다.
year_month_day = input()
year = year_month_day[0:2]
month = year_month_day[2:4]
day = year_month_day[4:6]
print(year, month, day, sep=' ')

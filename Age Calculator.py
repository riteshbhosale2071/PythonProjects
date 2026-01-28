import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28

name = input("input your name: ")
birth_year = int(input("input your birth year (YYYY): "))
birth_month = int(input("input your birth month (MM): "))
birth_day = int(input("input your birth day (DD): "))

localtime = time.localtime(time.time())

# calculate age in years
year = localtime.tm_year - birth_year
if (localtime.tm_mon, localtime.tm_mday) < (birth_month, birth_day):
    year -= 1

month = year * 12 + (localtime.tm_mon - birth_month)
if localtime.tm_mday < birth_day:
    month -= 1

day = 0
begin_year = birth_year
end_year = localtime.tm_year

# calculate the days from full years
for y in range(begin_year, end_year):
    if (judge_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

# subtract days before birthday in birth year
leap_year = judge_leap_year(birth_year)
for m in range(1, birth_month):
    day = day + month_days(m, leap_year)
day = day + birth_day

# add days in current year
leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)
day = day + localtime.tm_mday

print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))
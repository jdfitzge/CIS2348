# joshua fitzgerald 1374331

from datetime import date

print('Birthday Calculator')
print('Current day')


month = int(input('Enter a month'))
day = int(input('Enter a day'))
year = int(input('Enter a year'))
current_date =  date(year, month, day)

print('Birthday')

b_month = int(input('Enter a month'))
b_day = int(input('Enter a day'))
b_year = int(input('Enter a year'))
birth_date =  date(b_year, b_month, b_day)

y = current_date.year - birth_date.year
if current_date.month < birth_date.month or current_date.month == birth_date.month and current_date.day < birth_date.day:
    y -= 1
print('You are', y ,'years old.')


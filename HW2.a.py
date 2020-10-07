#joshua fitzgerald 1374331

import time

org_date= input('Enter a date in this format - March 1, 1992\n')
new_date=time.strptime(org_date,"%B %d, %Y")
time.strftime("%d/%m/%Y",new_date)

print(new_date.tm_mon,'/',new_date.tm_mday,'/',new_date.tm_year)

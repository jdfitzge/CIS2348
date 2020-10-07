#joshua fitzgerald 1374331
#restaurant occupancy
import math

org_occupancy = float(input('What was the building\'s total occupancy before covid?'))
print()

cov_occupancy =(float(input('What is the current occupancy % the governement is allowing? '))) / 100
print()

patrons = int(input('How many customers are already in the buidling?'))
print()

cur_occupancy = int((org_occupancy * cov_occupancy) - patrons)

print ('The restaurant can seat', cur_occupancy, 'more people.')

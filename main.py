#joshua fitzgerald 1374331

def exact_change(user_total):

    dollars = user_total//100
    user_total = user_total % 100
    quarters = user_total//25
    user_total = user_total % 25
    dimes = user_total//10
    user_total = user_total % 10
    nickels = user_total//5
    user_total = user_total % 5
    pennies = user_total

    return dollars, quarters, dimes, nickels, pennies

inputval = int(input())

dollars, quarters, dimes, nickels, pennies = exact_change(inputval)

if inputval == 0:
    print('no change')

if dollars == 1:
    print(dollars, "dollar")

elif dollars > 1:
    print(dollars, "dollars")

if quarters == 1:
    print(quarters, "quarter")

elif quarters > 1:
    print(quarters, "quarters")

if dimes == 1:
    print(dimes, "dime")
elif dimes > 1:
    print(dimes, "dimes")

if nickels == 1:
    print(nickels, "nickel")

elif nickels > 1:
    print(nickels, "nickels")

if pennies == 1:
    print(pennies, "penny")

elif pennies > 1:
    print(pennies, "pennies")
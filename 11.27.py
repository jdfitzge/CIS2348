#jdfitzge 1374331

roster = dict()
for i in range(5):
    print("Enter player " + str(i + 1) + "'s jersey number:")
    num = int(input())
    print("Enter player " + str(i + 1) + "'s rating:")
    rating = int(input())
    print()
    roster[num] = rating

sorted_players = sorted(roster.keys())
print('ROSTER')
for i in sorted_players:
    print("Jersey number: " + str(i) + ", Rating:", roster[i])

while (True):
    print()
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print()
    print('Choose an option:')
    option = input()

    if option == 'a':
        print("Enter a new player's jersey number:")
        num = int(input())
        print("Enter the player's rating:")
        rating = int(input())
        roster[num] = rating
    elif option == 'd':
        print('Enter a jersey number:')
        number = int(input())
        if number in roster:
            del roster[number]
    elif option == 'u':
        print("Enter a jersey number:")
        num = int(input())
        print("Enter a new rating for player:")
        rating = int(input())
        if num in roster:
            roster[num] = rating
        else:
            print('This jersey number is not in the roster.')
    elif option == 'r':
        print("Enter a rating:")
        rating = int(input())
        print()
        sorted_players = sorted(roster.keys())
        print('ABOVE', rating)
        for i in sorted_players:
            if roster[i] > rating:
                print("Jersey number: " + str(i) + ", Rating:", roster[i])
    elif option == 'o':
        sorted_players = sorted(roster.keys())
        print('ROSTER')
        for i in sorted_players:
            print("Jersey number: " + str(i) + ", Rating:", roster[i])
    elif option == 'q':
        break
    else:
        print("Choose another option.")

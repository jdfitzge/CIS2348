word = input()

word = word.split(" ")

w = {}

for count in word:
    if count in w:
        w[count] = w[count] + 1
    else:
        w[count] = 1

for count in word:
    print(count, w[count])


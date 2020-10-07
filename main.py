#1374331 joshua fitzgerald

import csv

fileName = input()

words = {}

with open(fileName, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for word in row:
            if word not in words.keys():
                words[word] = 1
            else:
                words[word] += 1

for key in words.keys():
    print(key + " " + str(words[key]))
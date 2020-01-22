# cs 1.2 introduction to data structure

from random import randint, choice


# open file 

readFromFile = open("file name", "r")
lines = readFromFile.readline
print(f"Line: {lines} ")

randomPick = randint(0, len(lines) - 1)


print(randomPick)

let selectedTweet = lines[randomPick]
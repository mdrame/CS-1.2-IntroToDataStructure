# cs 1.2 introduction to data structure

from random import randint, choice


# open file 

# readFromFile = open("file name", "r")
# lines = readFromFile.readline
# print(f"Line: {lines} ")


# List of worlds 
quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

def random_Number_Processing () :
# picked random index from the quotes array/list
    randomPick = randint(0, len(quotes) - 1)
# test
    # print(f"Random Number: {randomPick}")

# assing selected quote to a new variable
    selectedTweet = quotes[randomPick]
# test 
    # print(f"Selected Quote: {selectedTweet}")
    return selectedTweet




if __name__ == '__main__':
    quote = random_Number_Processing()
    print(f"Quote Selected: {quote}")
import random
import sys


def make__sentence(words=1):
    # getting words from file
    word_file = open("words.txt", "r")
    # read and slpit words into an array
    lines = word_file.read().split('\n')
   # empty array for amount of word paramenter request
    word_list = []

    # 
    while len(word_list) < words:
        word_list.append(random.choice(lines))

    return(' '.join(word_list))



if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(make__sentence(int(sys.argv[1])))
    else:
        print(make__sentence())








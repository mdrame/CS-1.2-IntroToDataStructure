# # Rearrange Words 

import sys
import random

# Write a script (rearrange.py), that randomly rearranges 
# a set of words provided as command-line arguments to the script.


# getting string input from command line
inputedWord = sys.argv[1:]
# shuffling the inputed string from command line 
random.shuffle(inputedWord)

# print shuffled string 
print(inputedWord)



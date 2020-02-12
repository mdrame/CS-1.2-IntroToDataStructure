# app.py
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/') #index
def dashBoard():


    return render_template("index.html")



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)


# open file 

# readFromFile = open("file name", "r")
# lines = readFromFile.readline
# print(f"Line: {lines} ")


# List of worlds 
# quotes = ("It's just a flesh wound.",
#           "He's not the Messiah. He's a very naughty boy!",
#           "THIS IS AN EX-PARROT!!")

# def random_Number_Processing () :
# # picked random index from the quotes array/list
#     randomPick = randint(0, len(quotes) - 1)
# # test
#     # print(f"Random Number: {randomPick}")

# # assing selected quote to a new variable
#     selectedTweet = quotes[randomPick]
# # test 
#     # print(f"Selected Quote: {selectedTweet}")
#     return selectedTweet






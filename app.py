from flask import Flask, render_template, request, redirect, url_for #Built in methods accessing
from histogram import histogram_dict, read_file # importing two methods from histogram
import random


app = Flask(__name__)

@app.route('/') #index
def display_phrase():
  # read_file method open a file, get string and slit them into words.
  words_list = read_file('testing.txt')
  # histograme_dict return a dictionary dictionary of words count.
  histogram = histogram_dict(words_list)


  return render_template('index.html', histogram=histogram) 



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=True)




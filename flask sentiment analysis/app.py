from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import joblib
import re
import string
import pythainlp
from pythainlp import word_tokenize, Tokenizer
import pickle

# Declare a Flask app
app = Flask(__name__) 

@app.route('/senti')
def home():
    return render_template('website.html')

@app.route('/senti', methods=['GET', 'POST'])
def main():
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        pipeline = joblib.load("pipeline.pkl")

        # load the model from disk
        customTokenizer = pickle.load(open("customTokenizer.pkl", 'rb'))
        
        newtext = request.form['text']

        # Tokenize 
        def LabelText(newText):
            tokenizer = customTokenizer.word_tokenize(newText)

            tokenizer = ','.join(map(str, tokenizer))

            tokenizer = [re.sub(r',',' ',tokenizer)]

            return tokenizer
            
        # Get prediction
        my_predict = pipeline.predict(LabelText(newtext))

    else:
        my_predict = ""

    return render_template("website.html", prediction = my_predict)

# Running the app
if (__name__)  == 'main':
    app.run(host="0.0.0.0", port=5000, debug=True)




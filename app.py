
import numpy  # Not directly used, but included for completeness
import scipy  # Not directly used, but included for completeness
from flask import Flask, render_template, request
from textblob import TextBlob

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')  # Specify the template folder


def sentiment_analysis(text):
    analysis = TextBlob(text).sentiment
    polarity = analysis.polarity
    subjectivity = analysis.subjectivity  # Added to retrieve subjectivity

    if polarity > 0.1:
        sentiment = "😊 Positive"
        sentiment_prob = polarity
    elif polarity < -0.1:
        sentiment = "😠 Negative"
        sentiment_prob = abs(polarity)
    else:
        sentiment = "😐 Neutral"
        sentiment_prob = 0.0


    # Include subjectivity for additional information (optional)
    return sentiment, sentiment_prob, subjectivity


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sentiment', methods=['POST'])
def sentiment():
    text = request.form['text']
    sentiment, sentiment_prob, subjectivity = sentiment_analysis(text)
    return render_template('index.html', sentiment=sentiment, sentiment_prob=sentiment_prob, subjectivity=subjectivity)


if __name__ == '__main__':
    app.run(debug=True)

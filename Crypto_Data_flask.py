# Crypto_Data.py

from flask import Flask, request, render_template


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/orderbook_bias')
def orderbook_bias():
    return render_template('orderbook_bias.html')

@app.route('/trader_bias')
def trader_bias():
    return render_template('trader_bias.html')

@app.route('/reddit_posts')
def reddit_posts():
    return render_template('reddit_posts.html')


if __name__ == '__main__':
    app.run()

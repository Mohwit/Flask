from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home'



if __name__ == '__main__':
    app.run(debug=True)
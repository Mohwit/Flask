## Building URL dynamically
## Variables rules and URL building

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return'Welcome'

## variable rules 
## create a route/url dynamically 
## using an integer data type for url
@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed and the score is ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has fail and the score is ' + str(score)


## creating result checker
## redirect used to redirect to a url
## url_for takes two paramter i,e location(pages) and a additional paramter/value
@app.route('/result/<int:marks>')
def results(marks):
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    
    return redirect(url_for(result, score = marks))

## main function 
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

## object of flask app
## wsgi application which interacts/communicating with the web server
app = Flask(__name__)

## decorator 
## takes two inputs i,e 1. rule 2.Option
@app.route('/')
## this function will get triggered for above route
def welcome():
    return "Welcome!"

@app.route('/members')
def members():
    return "Welcome members!"

## main function
if __name__ == '__main__':
    ## 'debug = True'refresh server automatical when you save a file
    app.run(debug=True)
### Jinja 2 template engine
''' 
{%..%} used for statement/condition (loops, if-else)
{{ }} used to print output
{#..#} used for commenting
'''

from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

## route for pass
@app.route('/success/<int:score>')
def success(score):
    return render_template('jinja2.html',result = score)

## route for fail
@app.route('/fail/<int:score>')
def fail(score):
    return render_template('jinja2.html',result = score)

## route for result
@app.route('/result/<int:score>')
def result(score):
    res = ''
    if score <= 50:
        res = 'FAIL'
    else:
        res = 'PASS'
    
    expression = {'Score':score, 'Result': res}

    return render_template('jinja2.html', result=expression)


## result checker html submit page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    ## for total score of all subject 
    total_score = 0 
    ## checking if request is POST
    if request.method == 'POST':
        ## taking data from form 
        math = float(request.form['math'])
        science = float(request.form['science'])
        comp_sci = float(request.form['computer-science'])
        data_sci = float(request.form['data-science'])

        ## adding all marks 
        total_score = (math + science + comp_sci + data_sci)

        ## calculating average
        average = total_score / 4

    ## for result 
    result = ''

    ##if average less than 50 
    if average >= 50:
        result = 'success'
    ##otherwise
    else:
        result = 'fail'
    
    ##redirecting
    ## generating dynamic url

    ## changing result to 'result for running expression part
    return redirect(url_for('result', score = average))


## main method
if __name__ == '__main__':
    app.run(debug=True)
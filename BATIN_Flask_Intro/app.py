from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def areaOfcircle():
    result = None
    if request.method == 'POST':
        input_int = int(request.form['inputNum'])
        result = math.pi*input_int**2
    return render_template('areaOfcircle.html', result=result)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def areaOfTriangle():
    result = None
    if request.method == 'POST':
        base = int(request.form['base'])
        height = int(request.form['height'])
        result = (base*height)/2
    return render_template('areaOfTriangle.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
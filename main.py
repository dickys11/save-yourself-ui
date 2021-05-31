from flask.helpers import url_for
import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        numpage = request.form['numpage']
        return redirect(url_for("result", username=username, numpage=numpage))
    else:
        return render_template('home.html')

@app.route('/result/<username>/<numpage>')
def result(username, numpage):
    r = requests.get(f'http://34.87.19.67:8888/getstatus/{username}/{numpage}')
    return render_template('result.html', r=r.json())

from flask import Flask
from flask import render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/sinclairCV')
def sinclairCV():
    return render_template('cv.html')

@app.route('/mdb')
def mdb():
    return render_template('mdb.html')

@app.route('/BondRobotics')
def BondRobotics():
    return render_template('BondRobotics.html')

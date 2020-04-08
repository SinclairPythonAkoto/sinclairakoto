import os

from flask import Flask, render_template, url_for, request, redirect
import requests
from functools import wraps
from flask_mail import Mail, Message
from payments import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sinclairCV')
def sinclairCV():
    return render_template('cv.html')

@app.route('/SinclairConnect', methods=['GET', 'POST'])
def SinclairConnect():
    if request.method == 'GET':
        return render_template('connect.html')
    else:
        txt = request.form.get('sendText')
        sender = request.form.get('senderName')
        contact = request.form.get('senderContact')
        from clockwork import clockwork
        api = clockwork.API(os.getenv('API_KEY'),)	# this has been left blank to protect API identity

        message = clockwork.SMS(
		    to = '447481790498',
		    message = f'{txt.lower()}\nFrom: {sender}, {contact}',
		    from_name='MrAkotoApps')

        response = api.send(message)

        if response.success:
            return render_template('connect.html', txt=txt, sender=sender, contact=contact)
        else:
            return redirect(url_for('SinclairConnect'))

@app.route('/demoshop')
def demoshop():
    return render_template('demoshop_home.html')

@app.route('/demoshop/jackets', methods=['GET', 'POST'])
def demoshop_jackets():
    if form.request == 'GET':
        return render_template('jackets.html')
    else:
        pass

if __name__ == '__main__':
   app.run(debug=True)

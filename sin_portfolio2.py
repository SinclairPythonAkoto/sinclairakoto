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
    header_title = "My Demo Shop"
    return render_template('demoshop_home.html', header_title=header_title)

@app.route('/jackets', methods=['GET', 'POST'])
def demoshop_jackets():
    header_title = "Jackets"
    if request.method == 'GET':
        return render_template('jackets.html', header_title=header_title)
    else:
        pass

@app.route('/black-gilet-purchase')
def black_gilet_purchase():
    return render_template('black_gilet.html', pub_key=pub_key)

@app.route('/black-gilet-checkout', methods=['POST'])
def black_gilet_checkout():
    name = request.form.get("Name")
    street = request.form.get("Street")
    city = request.form.get("City")
    postcode = request.form.get("Postcode")
    if street == '' and postcode == '':
        return "You need to enter your delivery address"
    else:
        from payments import BlackGilet_45gbp
        CEmail = request.form['stripeEmail']

        # Customer Email to send complimentary message
        myEmail = CEmail

        # return redirect(url_for('demoshop'))
        return f"Your package was sent to:{name}\n{street}\n{city}\n{postcode}\nprice: £45.00\nReciept sent to: {CEmail}"

if __name__ == '__main__':
   app.run(debug=True)

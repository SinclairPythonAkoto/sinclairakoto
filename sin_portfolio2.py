import os

from flask import Flask, render_template, url_for, request, redirect
import requests
from functools import wraps
from flask_mail import Mail, Message
from payments import *

app = Flask(__name__)

# Flask-Mail config
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = "sinclair.python@gmail.com",
    MAIL_PASSWORD = "Python2020",
    MAIL_DEFAULT_SENDER = ('BondRobotics'),
    MAIL_MAX_EMAILS = 25
))

mail = Mail(app)

# set session secret secret_key
app.secret_key = os.getenv("SECRET_KEY")


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
    from payments import BlackGilet_45gbp
    customer_name = request.form.get("Name")
    street = request.form.get("Street")
    city = request.form.get("City")
    postcode = request.form.get("Postcode")
    product = "ASOS Black Gilet"
    price = "£45.00"

    CEmail = request.form['stripeEmail']

    # Customer Email to send complimentary message
    myEmail = CEmail
    # sending an email to the customer
    msg = Message('Thank you for your purchase!', recipients=[myEmail]) # (Email subject, [Customer Email])
    msg.html = f"<p>Thank you {customer_name} for your recent purchase from My Demo Shop! This is an email confirming that you purchased an {product} for {price}.\n\nAs this is a demo version, you will not recieve a separate email from Stripe confirming your with a reference number.\nYour item(s) will be sent to {street}, {city}, {postcode} and will be dispatched to our courier soon.\nDeliveries usually take between 3 - 7 working days, if your delivery has taken longer than that please contact us with your reference number.\n\nAdditionally, if you would like to continue shopping at My Demo Shop please click <b><a href='https://www.sinclair.codes/demoshop'>here</a></b>.<br><br>\n\nTo leave a comment/review please click <b><a href='https://www.sinclair.codes/demoshop#demoshop_footer'>here</a></b>.</p>"
    # add an attachment logo/pdf etc to email
    with app.open_resource('BondRobotics_logo_crop.JPG') as logo:
        msg.attach('BondRobotics_logo_crop.JPG', 'image/jpeg', logo.read())
    mail.send(msg)

    return redirect(url_for('demoshop'))
    # return f"Your package was sent to:{name}\n\n{street}\n\n{city}\n\n{postcode}\n\nitem: {product}\n\nprice: {price}\n\nReciept sent to: {CEmail}"

if __name__ == '__main__':
   app.run(debug=True)

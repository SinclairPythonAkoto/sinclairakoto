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
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = "sinclair.python@gmail.com",
    MAIL_PASSWORD = os.getenv("GMAIL_PW"),
    MAIL_DEFAULT_SENDER = ('BondRobotics', "sinclair.python@gmail.com"),
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

@app.route('/jackets')
def demoshop_jackets():
    header_title = "Jackets"
    return render_template('jackets.html', header_title=header_title)

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
    msg.html = f"<p>Thank you {customer_name} for your recent purchase from My Demo Shop! This is an email confirming that you purchased an {product} for {price}.<br><br>As this is a demo version, you will not recieve a separate email from Stripe confirming your with a reference number.<br>Your item(s) will be sent to {street}, {city}, {postcode} and will be dispatched to our courier soon.<br>Deliveries usually take between 3 - 7 working days, if your delivery has taken longer than that please contact us with your reference number.<br><br>Additionally, if you would like to continue shopping at My Demo Shop please click <b><a href='https://www.sinclair.codes/demoshop'>here</a></b>.<br><br>To leave a comment/review please click <b><a href='https://www.sinclair.codes/demoshop#demoshop_footer'>here</a></b>.</p>"
    # add an attachment logo/pdf etc to email
    with app.open_resource('BondRobotics_logo_crop.JPG') as logo:
        msg.attach('BondRobotics_logo_crop.JPG', 'image/jpeg', logo.read())
    mail.send(msg)

    return redirect(url_for('demoshop'))

@app.route('/nike-swoosh-sweater-purchase')
def nike_swoosh_sweater_purchase():
    return render_template('nike_swoosh_sweater.html', pub_key=pub_key)

@app.route('/nike-swoosh-sweater-checkout', methods=['POST'])
def nike_swoosh_sweater_checkout():
    from payments import NikeSweater_55gbp
    customer_name = request.form.get("Name")
    street = request.form.get("Street")
    city = request.form.get("City")
    postcode = request.form.get("Postcode")
    product = "Grey Nike Swoosh Sweater"
    price = "£55.00"
    CEmail = request.form['stripeEmail']
    myEmail = CEmail
    msg = Message('Thank you for your purchase!', recipients=[myEmail])
    msg.html = f"<p>Thank you {customer_name} for your recent purchase from My Demo Shop! This is an email confirming that you purchased a {product} for {price}.<br><br>As this is a demo version, you will not recieve a separate email from Stripe confirming your with a reference number.<br>Your item(s) will be sent to {street}, {city}, {postcode} and will be dispatched to our courier soon.<br>Deliveries usually take between 3 - 7 working days, if your delivery has taken longer than that please contact us with your reference number.<br><br>Additionally, if you would like to continue shopping at My Demo Shop please click <b><a href='https://www.sinclair.codes/demoshop'>here</a></b>.<br><br>To leave a comment/review please click <b><a href='https://www.sinclair.codes/demoshop#demoshop_footer'>here</a></b>.</p>"
    with app.open_resource('BondRobotics_logo_crop.JPG') as logo:
        msg.attach('BondRobotics_logo_crop.JPG', 'image/jpeg', logo.read())
    mail.send(msg)
    return redirect(url_for('demoshop'))

@app.route('/nike-swoosh-tracksuit-purchase')
def nike_swoosh_tracksuit_purchase():
    return render_template('nike_swoosh_tracksuit.html', pub_key=pub_key)

@app.route('/nike-swoosh-tracksuit-checkout', methods=['POST'])
def nike_swoosh_tracksuit_checkout():
    from payments import NikeTracksuit_125gbp
    customer_name = request.form.get("Name")
    street = request.form.get("Street")
    city = request.form.get("City")
    postcode = request.form.get("Postcode")
    product = "Grey Nike Swoosh Sweater"
    price = "£125.00"
    CEmail = request.form['stripeEmail']
    myEmail = CEmail
    msg = Message('Thank you for your purchase!', recipients=[myEmail])
    msg.html = f"<p>Thank you {customer_name} for your recent purchase from My Demo Shop! This is an email confirming that you purchased a {product} for {price}.<br><br>As this is a demo version, you will not recieve a separate email from Stripe confirming your with a reference number.<br>Your item(s) will be sent to {street}, {city}, {postcode} and will be dispatched to our courier soon.<br>Deliveries usually take between 3 - 7 working days, if your delivery has taken longer than that please contact us with your reference number.<br><br>Additionally, if you would like to continue shopping at My Demo Shop please click <b><a href='https://www.sinclair.codes/demoshop'>here</a></b>.<br><br>To leave a comment/review please click <b><a href='https://www.sinclair.codes/demoshop#demoshop_footer'>here</a></b>.</p>"
    with app.open_resource('BondRobotics_logo_crop.JPG') as logo:
        msg.attach('BondRobotics_logo_crop.JPG', 'image/jpeg', logo.read())
    mail.send(msg)
    return redirect(url_for('demoshop'))

@app.route('/trousers')
def demoshop_trousers():
    header_title = "Trousers"
    return render_template('trousers.html', header_title=header_title)

@app.route('/nike-swoosh-joggers-purchase')
def nike_swoosh_joggers_purchase():
    return render_template('nike_joggers.html', pub_key=pub_key)

@app.route('/nike-swoosh-joggers-checkout', methods=['POST'])
def nike_swoosh_joggers_checkout():
    from payments import NikeJoggers_55gbp
    customer_name = request.form.get("Name")
    street = request.form.get("Street")
    city = request.form.get("City")
    postcode = request.form.get("Postcode")
    product = "Grey Nike Swoosh Joggers"
    price = "£55.00"
    CEmail = request.form['stripeEmail']
    myEmail = CEmail
    msg = Message('Thank you for your purchase!', recipients=[myEmail])
    msg.html = f"<p>Thank you {customer_name} for your recent purchase from My Demo Shop! This is an email confirming that you purchased a {product} for {price}.<br><br>As this is a demo version, you will not recieve a separate email from Stripe confirming your with a reference number.<br>Your item(s) will be sent to {street}, {city}, {postcode} and will be dispatched to our courier soon.<br>Deliveries usually take between 3 - 7 working days, if your delivery has taken longer than that please contact us with your reference number.<br><br>Additionally, if you would like to continue shopping at My Demo Shop please click <b><a href='https://www.sinclair.codes/demoshop'>here</a></b>.<br><br>To leave a comment/review please click <b><a href='https://www.sinclair.codes/demoshop#demoshop_footer'>here</a></b>.</p>"
    with app.open_resource('BondRobotics_logo_crop.JPG') as logo:
        msg.attach('BondRobotics_logo_crop.JPG', 'image/jpeg', logo.read())
    mail.send(msg)
    return redirect(url_for('demoshop'))

@app.route('/shirts')
def demoshop_shirts():
    header_title = "Shirts"
    return render_template('shirts.html', header_title=header_title)

@app.route('/stretch-slim-shirt-purchase')
def stretch_slim_shirt_purchase():
    return render_template('slim_shirt.html', pub_key=pub_key)

@app.route('/stretch-slim-shirt-checkout')
def stretch_slim_shirt_checkout():
    from payments import SlimShirt_18gbp
    customer_name = request.form.get("Name")
    street = request.form.get("Street")
    city = request.form.get("City")
    postcode = request.form.get("Postcode")
    product = "ASOS White Stretch Slim Shirt"
    price = "£18.00"
    CEmail = request.form['stripeEmail']
    myEmail = CEmail
    msg = Message('Thank you for your purchase!', recipients=[myEmail])
    msg.html = f"<p>Thank you {customer_name} for your recent purchase from My Demo Shop! This is an email confirming that you purchased a {product} for {price}.<br><br>As this is a demo version, you will not recieve a separate email from Stripe confirming your with a reference number.<br>Your item(s) will be sent to {street}, {city}, {postcode} and will be dispatched to our courier soon.<br>Deliveries usually take between 3 - 7 working days, if your delivery has taken longer than that please contact us with your reference number.<br><br>Additionally, if you would like to continue shopping at My Demo Shop please click <b><a href='https://www.sinclair.codes/demoshop'>here</a></b>.<br><br>To leave a comment/review please click <b><a href='https://www.sinclair.codes/demoshop#demoshop_footer'>here</a></b>.</p>"
    with app.open_resource('BondRobotics_logo_crop.JPG') as logo:
        msg.attach('BondRobotics_logo_crop.JPG', 'image/jpeg', logo.read())
    mail.send(msg)
    return redirect(url_for('demoshop'))

@app.route('/ps-shirt-purchase')
def ps_shirt_purcahse():
    return render_template('ps_shirt.html', pub_key=pub_key)

@app.route('/ps-shirt-checkout', methods=['POST'])
def ps_shirt_checkout():
    from payments import PaulSmithShirt_135gbp
    customer_name = request.form.get("Name")
    street = request.form.get("Street")
    city = request.form.get("City")
    postcode = request.form.get("Postcode")
    product = "Khaki Paul Smith Patchwork Pocket Shirt"
    price = "£135.00"
    CEmail = request.form['stripeEmail']
    myEmail = CEmail
    msg = Message('Thank you for your purchase!', recipients=[myEmail])
    msg.html = f"<p>Thank you {customer_name} for your recent purchase from My Demo Shop! This is an email confirming that you purchased a {product} for {price}.<br><br>As this is a demo version, you will not recieve a separate email from Stripe confirming your with a reference number.<br>Your item(s) will be sent to {street}, {city}, {postcode} and will be dispatched to our courier soon.<br>Deliveries usually take between 3 - 7 working days, if your delivery has taken longer than that please contact us with your reference number.<br><br>Additionally, if you would like to continue shopping at My Demo Shop please click <b><a href='https://www.sinclair.codes/demoshop'>here</a></b>.<br><br>To leave a comment/review please click <b><a href='https://www.sinclair.codes/demoshop#demoshop_footer'>here</a></b>.</p>"
    with app.open_resource('BondRobotics_logo_crop.JPG') as logo:
        msg.attach('BondRobotics_logo_crop.JPG', 'image/jpeg', logo.read())
    mail.send(msg)
    return redirect(url_for('demoshop'))

@app.route('/t-shirts')
def demoshop_tshirts():
    header_title = "T-Shirts"
    return render_template('tshirts.html', header_title=header_title)

@app.route('/ax-tshirt-purchase')
def ax_tshirt_purchase():
    return render_template('ax_shirt.html', pub_key=pub_key)

@app.route('/ax-tshirt-checkout', methods=['POST'])
def ax_tshirt_checkout():
    from payments import ArmaniExchangeTshirt_35gpb
    customer_name = request.form.get("Name")
    street = request.form.get("Street")
    city = request.form.get("City")
    postcode = request.form.get("Postcode")
    product = "Red Armani Exchange AX Text Logo T-shirt"
    price = "£35.00"
    CEmail = request.form['stripeEmail']
    myEmail = CEmail
    msg = Message('Thank you for your purchase!', recipients=[myEmail])
    msg.html = f"<p>Thank you {customer_name} for your recent purchase from My Demo Shop! This is an email confirming that you purchased a {product} for {price}.<br><br>As this is a demo version, you will not recieve a separate email from Stripe confirming your with a reference number.<br>Your item(s) will be sent to {street}, {city}, {postcode} and will be dispatched to our courier soon.<br>Deliveries usually take between 3 - 7 working days, if your delivery has taken longer than that please contact us with your reference number.<br><br>Additionally, if you would like to continue shopping at My Demo Shop please click <b><a href='https://www.sinclair.codes/demoshop'>here</a></b>.<br><br>To leave a comment/review please click <b><a href='https://www.sinclair.codes/demoshop#demoshop_footer'>here</a></b>.</p>"
    with app.open_resource('BondRobotics_logo_crop.JPG') as logo:
        msg.attach('BondRobotics_logo_crop.JPG', 'image/jpeg', logo.read())
    mail.send(msg)
    return redirect(url_for('demoshop'))

@app.route('/nike-swoosh-tshirt-purchase')
def nike_swoosh_tshirt_purchase():
    return render_template('nike_tshirt.html', pub_key=pub_key)

@app.route('/nike-swoosh-tshirt-checkout', methods=['POST'])
def nike_swoosh_tshirt_checkout():
    from payments import NikeTshirt_19gbp
    customer_name = request.form.get("Name")
    street = request.form.get("Street")
    city = request.form.get("City")
    postcode = request.form.get("Postcode")
    product = "Nike White Swoosh T-Shirt"
    price = "£19.95"
    CEmail = request.form['stripeEmail']
    myEmail = CEmail
    msg = Message('Thank you for your purchase!', recipients=[myEmail])
    msg.html = f"<p>Thank you {customer_name} for your recent purchase from My Demo Shop! This is an email confirming that you purchased a {product} for {price}.<br><br>As this is a demo version, you will not recieve a separate email from Stripe confirming your with a reference number.<br>Your item(s) will be sent to {street}, {city}, {postcode} and will be dispatched to our courier soon.<br>Deliveries usually take between 3 - 7 working days, if your delivery has taken longer than that please contact us with your reference number.<br><br>Additionally, if you would like to continue shopping at My Demo Shop please click <b><a href='https://www.sinclair.codes/demoshop'>here</a></b>.<br><br>To leave a comment/review please click <b><a href='https://www.sinclair.codes/demoshop#demoshop_footer'>here</a></b>.</p>"
    with app.open_resource('BondRobotics_logo_crop.JPG') as logo:
        msg.attach('BondRobotics_logo_crop.JPG', 'image/jpeg', logo.read())
    mail.send(msg)
    return redirect(url_for('demoshop'))

@app.route('/shoes')
def demoshop_shoes():
    header_title = "Shoes"
    return render_template('shoes.html', header_title=header_title)

@app.route('/topman-loafers-purchase')
def topman_loafers_purchase():
    return render_template('topman_loafers.html', pub_key=pub_key)

@app.route('/topman-loafers-checkout')
def topman_loafers_checkout():
    from payments import TopmanLoafers_35gbp
    customer_name = request.form.get("Name")
    street = request.form.get("Street")
    city = request.form.get("City")
    postcode = request.form.get("Postcode")
    product = "Topman Black Velvet Loafers"
    price = "£35.00"
    CEmail = request.form['stripeEmail']
    myEmail = CEmail
    msg = Message('Thank you for your purchase!', recipients=[myEmail])
    msg.html = f"<p>Thank you {customer_name} for your recent purchase from My Demo Shop! This is an email confirming that you purchased a {product} for {price}.<br><br>As this is a demo version, you will not recieve a separate email from Stripe confirming your with a reference number.<br>Your item(s) will be sent to {street}, {city}, {postcode} and will be dispatched to our courier soon.<br>Deliveries usually take between 3 - 7 working days, if your delivery has taken longer than that please contact us with your reference number.<br><br>Additionally, if you would like to continue shopping at My Demo Shop please click <b><a href='https://www.sinclair.codes/demoshop'>here</a></b>.<br><br>To leave a comment/review please click <b><a href='https://www.sinclair.codes/demoshop#demoshop_footer'>here</a></b>.</p>"
    with app.open_resource('BondRobotics_logo_crop.JPG') as logo:
        msg.attach('BondRobotics_logo_crop.JPG', 'image/jpeg', logo.read())
    mail.send(msg)
    return redirect(url_for('demoshop'))

@app.route('/fred-perry-loafers-purchase')
def fred_perry_loafers_purchase():
    return render_template('fred_perry_loafers.html', pub_key=pub_key)

@app.route('/fred-perry-loafers-checkout', methods=['POST'])
def fred_perry_loafers_checkout():
    from payments import FredPerryLoafers_135gbp
    customer_name = request.form.get("Name")
    street = request.form.get("Street")
    city = request.form.get("City")
    postcode = request.form.get("Postcode")
    product = "Black Fred Perry George Cox Tassle Leather Loafers"
    price = "£135.00"
    CEmail = request.form['stripeEmail']
    myEmail = CEmail
    msg = Message('Thank you for your purchase!', recipients=[myEmail])
    msg.html = f"<p>Thank you {customer_name} for your recent purchase from My Demo Shop! This is an email confirming that you purchased a {product} for {price}.<br><br>As this is a demo version, you will not recieve a separate email from Stripe confirming your with a reference number.<br>Your item(s) will be sent to {street}, {city}, {postcode} and will be dispatched to our courier soon.<br>Deliveries usually take between 3 - 7 working days, if your delivery has taken longer than that please contact us with your reference number.<br><br>Additionally, if you would like to continue shopping at My Demo Shop please click <b><a href='https://www.sinclair.codes/demoshop'>here</a></b>.<br><br>To leave a comment/review please click <b><a href='https://www.sinclair.codes/demoshop#demoshop_footer'>here</a></b>.</p>"
    with app.open_resource('BondRobotics_logo_crop.JPG') as logo:
        msg.attach('BondRobotics_logo_crop.JPG', 'image/jpeg', logo.read())
    mail.send(msg)
    return redirect(url_for('demoshop'))

@app.route('/trainers')
def demoshop_trainers():
    header_title = "Trainers"
    return render_template('trainers.html', header_title=header_title)



if __name__ == '__main__':
   app.run(debug=True)

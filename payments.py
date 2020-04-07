import os

# test keys
pub_key = os.getenv('PUB_KEY')
secret_key = os.getenv('SECRET_KEY')

# functions to take different amounts of payments from stripe below

def BlackGilet_45gbp():
    # creating a customer
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])

    # creating a charge to the customer
    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 4500,
        currency = 'gbp',
        description = '£45 ASOS Black Gilet white italic print'
    )

def NikeSweater_55gbp():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 5500,
        currency = 'gbp',
        description = '£55 Grey Nike Swoosh crew neck sweater'
    )

def NikeTracksuit_125gbp():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 12500,
        currency = 'gbp',
        description = '£125 Khaki Nike Swoosh tracksuit'
    )

def NikeJoggers_55gbp():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 5500,
        currency = 'gbp',
        description = '£55 Grey Nike Swoosh joggers'
    )

def SlimShirt_18gbp():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 1800,
        currency = 'gbp',
        description = '£18 ASOS white stretch slim shirt'
    )

def PaulSmithShirt_135gbp():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 13500,
        currency = 'gbp',
        description = '£135 Khaki Paul Smith patchwork pocket shirt'
    )

def ArmaniExchangeTshirt_35gpb():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 3500,
        currency = 'gbp',
        description = '£35 Red Armani Exchange AX text logo T-shirt'
    )

def NikeTshirt_19gbp():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 1995,
        currency = 'gbp',
        description = '£19.95 White Nike Swoosh logo T-shirt'
    )

def FredPerryLoafers_135gbp():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 13500,
        currency = 'gbp',
        description = '£135 Black Fred Perry George Cox tassle leather loafers'
    )

def TopmanLoafers_35gbp():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 3500,
        currency = 'gbp',
        description = '£35 Black velvet Topman loafers'
    )

def NikeAirMax90_114gbp():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 11495,
        currency = 'gbp',
        description = '£114.95 White/Purple Air Max 90'
    )

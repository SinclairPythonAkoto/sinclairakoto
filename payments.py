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
        amount = 5500,
        currency = 'gbp',
        description = '£125 Khaki Nike Swoosh tracksuit'
    )

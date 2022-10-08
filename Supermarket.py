# supermarket software

##Enter products and quantity with a while loop because the number of iterations is not known

def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input('Press A to add product and Q to quit: ')
        #if the cashier hits 'A' we define two variables (product, quantity) which gets added to the dictionary using the update() method
        if details == 'A':
            product = input('Enter product: ')
            quantity = int(input('Enter quantity: '))
            buyingData.update({product: quantity})
        #If cashier hits 'Q' then enterDetails gets updated to False which will break the loop
        elif details == 'Q':
            enterDetails = False
        #If cashier fails to enter 'A' or 'Q' then an error messge gets displayed. this does not break the loop.
        else:
            print('Please select a correct option')
        #return the dictionary containing product and quantity
    return buyingData

def getPrice(product, quantity):
    #defined dictionary with product as key and price as value
    priceData = {
        'Biscuit': 3,
        'Chicken': 5,
        'Egg': 1,
        'Fish': 3,
        'Coke': 2,
        'Bread': 2,
        'Apple': 3,
        'Onion': 3
    }
    #fetch corresponding value and multiply with quantity to get the subtotal
    subtotal = priceData[product] * quantity
    print(product + ':$' + str(priceData[product]) + 'x' + str(quantity) + '=' + str(subtotal))
    return subtotal

def getDiscount(billAmount, membership):
    #discount by default is 0 unless the subtotal is >= $25
    discount = 0
    if billAmount >= 25:
        # if subtotal is >= $25 we check for the membership and apply the appropriate disount
        if membership == 'Gold':
            billAmount = billAmount * 0.80
            discount = 20
        elif membership == 'Silver':
            billAmount = billAmount * 0.90
            discount = 10
        elif membership == 'Bronze':
            billAmount = billAmount * 0.95
            discount = 5
        print(str(discount) + '% off for ' + membership + ' ' + 'membership on total amount: $' + str(billAmount))
    else:
        print('No discount on amount less than $25')
    return billAmount

def makeBill(buyingData, membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    billAmount = getDiscount(billAmount, membership)
    print('The discounted amount is $' + str(billAmount))

buyingData = enterProducts()
membership = input('Enter customer membership: ')
makeBill(buyingData, membership)
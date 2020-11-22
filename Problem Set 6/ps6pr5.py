#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities    
#
# Computer Science 111
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]


def avg_price(prices):
    '''Option 3: This function takes a list of 1 or more prices
    and returns the average price'''
    tsum = 0
    for i in range(len(prices)):
        tsum += prices[i]
    return tsum/len(prices)
        
def std_dev(prices):
    '''Option 4: This function takes a list of 1 or more prices and 
    returns the standard deviation of the prices'''
    tsum = 0
    for i in range(len(prices)):
        a = (prices[i]-avg_price(prices))**2
        tsum += a
    val = tsum/len(prices)
    return math.sqrt(val)


def max_day(prices):
    '''Option 5: This function takes a list of 1 or more prices,
    and returns the day(index) of the maximum price'''
    a = prices[0]
    b = 0
    for i in range(len(prices)):
        if a<prices[i]:
            a = prices[i]
            b = i
    return b
            
def any_lower(prices, val):
    '''Option 6: This function takes a list of 1 or more prices 
    and an integer threshold, and determines if there are any prices lower 
    than that threshold. It returns true if there are any prices below the threshold, 
    or False otherwise'''
    for i in range(len(prices)):
        if prices[i]<val:
            return True
    return False

def find_tts(prices):
    '''Option 7: This function takes a list of 2 or more prices, and finds the best days 
    on which to buy and sell the stock whose prices are given in the list of prices.'''
    val = (-prices[0] + prices[0])
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            t = (-prices[i]+prices[j])
            if t>val:
                val = t
                a = i
                b = j
    return [a,b,val]

def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        elif choice ==3:
            averagep = avg_price(prices)
            print('The average price is', averagep)
        elif choice ==4:
            stdp = std_dev(prices)
            print('The standard deviation is', stdp)
        elif choice == 5:
            maxp = max_day(prices)
            print('The max price is', prices[maxp], 'on day', maxp)
        elif choice == 6:
            a = int(input('Enter the threshold: '))
            result = any_lower(prices, a)
            if result == True:
                print('There is at least one price below', a)
            else:
                print('There are no prices below', a)
        elif choice == 7:
            ans = find_tts(prices)
            print('Buy on day',ans[0], 'at price', prices[ans[0]])
            print('Sell on day',ans[1], 'at price',prices[ans[1]] )
            print('Total profit: ', ans[2])
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')

#!/usr/bin/env python3
from random import *

# function that starts game
def startGame():
    print()
    print('WHEW! IT\'S HOT OUT. And you\'re broke!')
    print('With only $10.00 left in your Venmo balance, you think to yourself... \n\"What can I do to make money today?\"')
    print("So... you decide to start a lemonade stand!")
    answer = input('\nAre YOU ready to make some cash? $$$ (y/n) ')
    answer = answer[0].lower()

    # loop that runs when user does not enter 'y' or 'n'
    while not (answer == 'y' or answer == 'n'):
        print("It's not a huge decision:")
        print("you either want to start a lemonade stand,")
        print("or you don't.")
        answer = input ("Interested? (y/n) ")
        answer = answer[0].lower()

    # evaluates user answer
    if answer == 'n':
        print("Totally understandable. The hustle isn't for everyone.")
        quit = True
    else:
        print("\nGreat! Get out some posterboard, your markers,")
        print("and get ready to make some cash!")
        print()
        print()
        quit = False
        print("Press ENTER to continue...")
        print()
        input()

    return quit

# function that defines rules
def rules():
    rules = ['1. Each day, you will receive a weather forecast', '2. Based on the forecast, you will decide how much lemonade to make', '3. But be careful! Precipitation, temperature, and price all affect sales', '4. Luckily, a heatwave guarantees your lemonade will sell out!', '5. A thunderstorm dampens business for the day, meaning no sales at all :\'(', 'Are you ready to get rich?!']
    print('OK. So here are the rules:')
    for rule in rules:
        print(rule)
    print()
    print('\nPress ENTER to continue...')
    print()
    input()

# function to generate daily weather, probability of each outcome, PPU, temp for next day. Day is a global variable
def newDay():
    global day

    forecast = ['heat wave', 'thunderstorm', 'sunny', 'cloud']
    sunny = randint(1, 100)
    if sunny < 100:
        maxCloudy = 100 - sunny
        cloudy = randint(1, maxCloudy)
        maxHeatWave = 100 - sunny - cloudy
        if maxHeatWave > 0:
           heatWave = randint(1, maxHeatWave)
        else:
            heatWave = 0
    else:
        cloudy = 0
        heatWave = 0
    thunderstorm = 100 - sunny - cloudy - heatWave

    weather = choices(forecast, weights=(heatWave, thunderstorm, sunny, cloudy), k=1)
    weather = weather[0]
    # initialize lemonadeCost variable and potential COGS
    lemonadeCost = round(uniform(0.25, 1.50) // 0.25 * 0.25, 2)  # Adjusted cost to a value divisible by $0.25 and less than $1.50
    temperature = randint(50, 100)

    day += 1

    return weather, lemonadeCost, temperature, sunny, cloudy, heatWave, thunderstorm

# function to display the forecast that accepts 5 weather conditions as arguments, also prints day no. at top of forecast
# this function does not return any values to the calling statement
def forecast(temperature, sunny, cloudy, heatWave, thunderstorm):
    global day

    print('Day '+str(day)+':')
    print()
    print('Tomorrow\'s forecast: ')
    print('Temp: '+str(temperature)+'°F')
    print('Sun: '+str(sunny)+'% chance')
    print('Clouds: '+str(cloudy)+'% chance')
    print('Heat Wave: '+str(heatWave)+'% chance')
    print('Storm: '+str(thunderstorm)+'% chance')
    print()
    print('Cost to make lemonade today: $'+str("{:.2f}".format(lemonadeCost)))
    print()
    print()
    print('Press ENTER to continue...')
    print()
    input()

# function to display choice menu
def menu():
    print('What would you like to do next?')
    print('1. Sell lemonade')
    print('2. Make lemonade')
    print('3. Close for the day')
    print('4. Forecast')
    print('5. Rules')
    print('6. Quit')

    # asks player for choice
    choice = input('Please enter a number: ')
    # tests of choice is a digit and converts to an integer
    if choice.isdigit():
        choice = int(choice)

    # tests choice and re-prompts user to enter a valid choice
    while choice not in range(1, 7):
        print('I\'m sorry, that\'s not a valid choice!')
        print('Valid choices are 1-6')
        choice = input('Please enter a number: ')
        if choice.isdigit():
            choice = int(choice)

    # once valid choice entered, returns entered choice to function
    return choice

# function to make lemonade, and modify cash and lemonade global variables. Does not receive or return any variables. Requires lemonadeCost argument to run
def makeLemonade(lemonadeCost):
    global lemonade
    global cash

    print()
    print('Alrightey! It\'s time to wash your hands, because \nwe\'re about to make some lemonade! \n\nHere\'s what you need to know:')
    print('Cost to make lemonade today: $'+str("{:.2f}".format(lemonadeCost)))
    print('Cash on hand: $'+str("{:.2f}".format(cash)))
    # asks player how much lemonade want to make
    cups = input('How many cups of lemonade would you like to make? ')
    # adds cups to lemonade variable
    lemonade += int(cups)
    # calculates cost of cups made
    cost = lemonadeCost * int(cups)
    # subtracts cost from player's cash
    cash -= cost

    print('You have made '+cups+' cups of lemonade! This cost you $'+str("{:.2f}".format(cost)))
    print()
    print('Inventory: '+str(lemonade)+' cups of lemonade')
    print('Cash on hand: $'+str("{:.2f}".format(cash)))
    print()
    print()
    print('Press ENTER to continue...')
    print()
    input()

# function to sell lemonade
# receives weather, lemonadeCost, and temperature variables to do calculation
def sellLemonade(weather, lemonadeCost, temperature):
    global lemonade

    print()
    print('Maximum price: $10.00')
    print()
    # asks player to set price
    valid_price = False
    while not valid_price:
        try:
            price = round(float(input('How many dollars would you like to charge per cup? $')), 2)
            if 0 < price <= 10.00:
                valid_price = True
            else:
                print('Please enter a price between $0.01 and $10.00')
        except ValueError:
            print('Invalid input. Please enter a valid price.')

    # calculates demand depending on weather
    if weather == 'heat wave':
        demand = lemonade
    elif weather == 'thunderstorm':
        demand = 0
    else:
        cupsSold = randint(1, 100)
        # 10% less demand for each $1 increase in price
        priceFactor = float(100 - price) / 100
        # 20% less demand for each degree under 100°F
        heatFactor = 1 - (((100 - temperature) * 2) / float(100))
        demand = cupsSold * priceFactor * heatFactor

    # changes demand +- 10% if sunny or cloudy
    # must be separate if statements because depend on output of demand variable
    if weather == 'sunny':
        demand *= 1.1
    if weather == 'cloudy':
        demand *= 0.9

    demand = int(round(demand, 0))

    # sets cupsSold to appropriate inventory level
    if demand < lemonade:
        cupsSold = demand
    elif demand >= lemonade:
        cupsSold = lemonade

    # displays appropriate message to player based on outcome
    if weather == 'thunderstorm':
        print()
        print('Unfortunately, a thunderstorm kept your lemonade stand closed!')
    elif weather == 'heat wave':
        print()
        print('Thanks to the heat wave, you have sold out for the day!')
    elif lemonade == 0:
        print()
        print('You had 0 cups in inventory! No loss, no gain!')
    elif cupsSold > lemonade:
        print()
        print('You sold out! You had '+str(lemonade)+' extra cup leftover.')
        print('Seeing there was demand for '+str(demand)+' cups, make more lemonade next time!')
    elif cupsSold == lemonade:
        print()
        print('You sold out! You had '+str(lemonade)+' cups in inventory \nand there was demand for '+str(demand)+' cups!')
        print('Clearly you have a great mind for business!')
    elif cupsSold < lemonade:
        print()
        print('Too bad! You had '+str(lemonade)+' cups in inventory and \nthere was demand for '+str(demand)+' cups.')
        print('Not a great sales day, but there\'s always tomorrow!')

    # calls calculateProfits function with required arguments
    calculateProfits(cupsSold, demand, price)

# function to calculate profits that accepts 3 arguments
def calculateProfits(cupsSold, demand, price):
    global cash
    global lemonade

    # tests if inventory exists and calculates profit
    if lemonade > 0:
        profit = round(cupsSold * price, 2)
        # increments profit variable
        cash += profit
        # increments inventory variable
        lemonade -= cupsSold
        print()
        print('Cups sold: '+str(cupsSold))
        print('Profit: $'+str("{:.2f}".format(profit)))
        print()

    # statements that print regardless of any conditions
    print('Cash on hand: $'+str("{:.2f}".format(cash)))
    print()
    print()
    print('Press ENTER to continue to next day...')
    print()
    input()

# main code for game
quit = startGame()

if not quit:
    rules()

day = 0
cash = 10
lemonade = 0

# main loop when player selects 'y'; calls, captures, and prints information from newDay function
while not quit:
    # variable used in interior loop for option '3'
    wait = False
    weather, lemonadeCost, temperature, sunny, cloudy, heatWave, thunderstorm = newDay()
    # calls forecast function and provides necessary arguments
    forecast(temperature, sunny, cloudy, heatWave, thunderstorm)
    # calls menu function and captures player's choice in a variable
    choice = menu()
    # interior loop for menu options that are not '1'
    while choice > 1:
        if choice == 6:
            # quit the game
            quit = True
            break
        elif choice == 5:
            rules()
            choice = menu()
            continue
        elif choice == 4:
            forecast(temperature, sunny, cloudy, heatWave, thunderstorm)
            choice = menu()
            continue
        elif choice == 3:
            # close for the day
            wait = True
            break
        elif choice == 2:
            makeLemonade(lemonadeCost)
            choice = menu()
            continue
    # evaluates 'quit' and 'wait' outcomes of menu loop
    if quit:
        break
    elif wait:
        continue
    # calls sellLemonade function if neither are true
    else:
        sellLemonade(weather, lemonadeCost, temperature)

totalProfit = cash - 10
if totalProfit > 0:
    print()
    print('Wow, you increased your net worth by $'+str("{:.2f}".format(totalProfit))+'!')
    print('You\'re well on your way to being rich!')
    print('If you\'re ever broke again, you can always sell lemonade!')
elif totalProfit == 0:
    print()
    print('You\'re ending where you started. You still have $10.00.')
    print('And now you know how to run a business!')
elif totalProfit < 0:
    print()
    print('Maybe sales isn\'t your thing...')
    print('You should probably get looking for a job.')
    print('It\'s going to be a long road to paying back the bank!')

print()
print("Goodbye!")
print()
print()

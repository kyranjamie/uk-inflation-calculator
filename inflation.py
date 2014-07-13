from datetime import datetime
import sys
import json

def calculateInflation():
    data = loadJson()    
    inputYear = input('Enter year to calculate from: ')
    inputYear = int(inputYear)
    amount = input('Amount of money then: ')
    amount = int(amount)
    currentYear =  datetime.now().year
    
    for year in range(inputYear + 1, currentYear):
        amount = amount * (data[str(year)] / 100 + 1)
    
    print('In today\'s money this would worth: ', '£%.2f' % round(amount, 2))

def loadJson():
    data = json.loads(open('inflation-data.json').read())
    return data
 
calculateInflation()

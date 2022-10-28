import random

rate_data = []
rate_list = [
    "Was Pong fun?",
    "Was Blackjack fun?",
    "Was Snake fun?",
    'Was the Jokebox fun?'
]

# Initialize True False
def initRate():
    # setup jokes into a dictionary with id, trfa, true, false
    item_id = 0
    for item in rate_list:
        rate_data.append({"id": item_id, "rate": item, "yes": 0, "no": 0})
        item_id += 1
    # prime some true responses
    for i in range(10):
        id = getRandomRate()['id']
        addRateYes(id)
    # prime some false responses
    for i in range(5):
        id = getRandomRate()['id']
        addRateNo(id)
        
# Return all jokes from jokes_data
def getRates():
    return(rate_data)

# Joke getter
def getRate(id):
    return(rate_data[id])

# Return random joke from jokes_data
def getRandomRate():
    return(random.choice(rate_data))

# Liked joke
def favoriteRate():
    best = 0
    bestID = -1
    for rate in getRates():
        if rate['yes'] > best:
            best = rate['yes']
            bestID = rate['id']
    return rate_data[bestID]
    
# Jeered joke
def worstRate():
    worst = 0
    worstID = -1
    for rate in getRates():
        if rate['false'] > worst:
            worst = rate['no']
            worstID = rate['id']
    return rate_data[worstID]

# Add to haha for requested id
def addRateYes(id):
    rate_data[id]['yes'] = rate_data[id]['yes'] + 1
    return rate_data[id]['yes']

# Add to boohoo for requested id
def addRateNo(id):
    rate_data[id]['no'] = rate_data[id]['no'] + 1
    return rate_data[id]['no']

# Pretty Print joke
def printRate(rate):
    print(rate['id'], rate['rate'], "\n", "yes:", rate['yes'], "\n", "no:", rate['no'], "\n")

# Number of jokes
def countRate():
    return len(rate_data)

# Test Joke Model
if __name__ == "__main__": 
    initRate()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteRate()
    print("Most liked", best['yes'])
    printRate(best)
    worst = worstRate()
    print("Most disliked", worst['no'])
    printRate(worst)
    
    # Random joke
    print("Random Game Rating")
    printRate(getRandomRate())
    
    # Count of Jokes
    print("Rate Count: " + str(countRate()))
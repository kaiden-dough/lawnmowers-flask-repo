import random

trfa_data = []
trfa_list = [
    "In the animation film “Finding Nemo,” the main protagonist is a pufferfish.",
    "Is Mount Kilimanjaro the world’s tallest peak?",
    "Spaghetto is the singular form of the word spaghetti.",
    "Pinocchio was Walt Disney’s first animated feature film in full color.",
    "Venezuela is home to the world’s highest waterfall.",
    "Coffee is a berry-based beverage.",
    "The capital of Australia is Sydney.",
    "The longest river in the world is the Amazon River.",
    "Polar bears can only live in the Arctic region, not in the Antarctic.",
    "The United Kingdom is almost the same size as France.",
    "Walt Disney has the record for most Academy Awards.",
    "By lying a frog on its back and softly caressing its tummy, it is possible to hypnotize it.",
    "The moon is wider than Australia.",
    "Daily, your nose and sinuses create almost one liter of mucus.",
    "Seahorses have stomachs, which aid in the digestion of food.",
    "The first Disney princess was Cinderella.",
    "In Scotland, the unicorn is their national animal.",
    'Zeus is referred to as the king of the Greek gods and goddesses.'
]

# Initialize True False
def initTrfa():
    # setup jokes into a dictionary with id, trfa, true, false
    item_id = 0
    for item in trfa_list:
        trfa_data.append({"id": item_id, "trfa": item, "true": 0, "false": 0})
        item_id += 1
    # prime some true responses
    for i in range(10):
        id = getRandomTrfa()['id']
        addTrfaTrue(id)
    # prime some false responses
    for i in range(5):
        id = getRandomTrfa()['id']
        addTrfaFalse(id)
        
# Return all jokes from jokes_data
def getTrfas():
    return(trfa_data)

# Joke getter
def getTrfa(id):
    return(trfa_data[id])

# Return random joke from jokes_data
def getRandomTrfa():
    return(random.choice(trfa_data))

# Liked joke
def favoriteTrfa():
    best = 0
    bestID = -1
    for trfa in getTrfas():
        if trfa['true'] > best:
            best = trfa['true']
            bestID = trfa['id']
    return trfa_data[bestID]
    
# Jeered joke
def worstTrfa():
    worst = 0
    worstID = -1
    for trfa in getTrfas():
        if trfa['false'] > worst:
            worst = trfa['boohoo']
            worstID = trfa['id']
    return trfa_data[worstID]

# Add to haha for requested id
def addTrfaTrue(id):
    trfa_data[id]['true'] = trfa_data[id]['true'] + 1
    return trfa_data[id]['true']

# Add to boohoo for requested id
def addTrfaFalse(id):
    trfa_data[id]['false'] = trfa_data[id]['false'] + 1
    return trfa_data[id]['false']

# Pretty Print joke
def printTrfa(trfa):
    print(trfa['id'], trfa['joke'], "\n", "true:", joke['true'], "\n", "false:", joke['false'], "\n")

# Number of jokes
def countTrfa():
    return len(trfa_data)

# Test Joke Model
if __name__ == "__main__": 
    initTrfa()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteTrfa()
    print("Most liked", best['true'])
    printTrfa(best)
    worst = worstTrfa()
    print("Most disliked", worst['false'])
    printTrfa(worst)
    
    # Random joke
    print("Random True or False Question")
    printTrfa(getRandomTrfa())
    
    # Count of Jokes
    print("True/False Count: " + str(countTrfa()))
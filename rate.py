from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_rate import *

app_api2 = Blueprint('apirate', __name__,
                   url_prefix='/api/rate')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api2 = Api(app_api2)

class RateAPI:
    # not implemented
    class _Create(Resource):
        def post(self, rate):
            pass
            
    # getJokes()
    class _Read(Resource):
        def get(self):
            return jsonify(getRates())

    # getJoke(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getRate(id))

    # getRandomJoke()
    
    
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomRate())
    
    class _ReadPong(Resource):
        def get(self):
            return jsonify(getPongRate())
    
    class _ReadBlackjack(Resource):
        def get(self):
            return jsonify(getBlackjackRate())
    
    class _ReadSnake(Resource):
        def get(self):
            return jsonify(getSnakeRate())
    
    class _ReadJokebox(Resource):
        def get(self):
            return jsonify(getJokeboxRate())
        
    
    # getRandomJoke()
    class _ReadCount(Resource):
        def get(self):
            count = countRate()
            countMsg = {'count': count}
            return jsonify(countMsg)

    # put method: addJokeHaHa
    class _UpdateLike(Resource):
        def put(self, id):
            addRateYes(id)
            return jsonify(getRate(id))

    # put method: addJokeBooHoo
    class _UpdateJeer(Resource):
        def put(self, id):
            addRateNo(id)
            return jsonify(getRate(id))

    # 2building RESTapi resources/interfaces, these routes are added to Web Server
    api2.add_resource(_Create, '/create/<string:rate>')
    api2.add_resource(_Read, '/')
    api2.add_resource(_ReadID, '/<int:id>')
    api2.add_resource(_ReadRandom, '/random')
    api2.add_resource(_ReadPong, '/pong')
    api2.add_resource(_ReadBlackjack, '/blackjack')
    api2.add_resource(_ReadSnake, '/snake')
    api2.add_resource(_ReadJokebox, '/jokebox')
    api2.add_resource(_ReadCount, '/count')
    api2.add_resource(_UpdateLike, '/like/<int:id>')
    api2.add_resource(_UpdateJeer, '/worst/<int:id>')
    
if __name__ == "__main__": 
    server = 'https://lawnmowers.nighthawkcodescrums.gq' # run local
    # server = 'https://flask.nighthawkcodingsociety.com' # run from web
    url = server + "/api/rate"
    responses = []  # responses list

    # get count of jokes on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update likes/dislikes test sequence
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  # read joke by id
        ) 
    responses.append(
        requests.put(url+"/like/"+num) # add to like count
        ) 
    responses.append(
        requests.put(url+"/worst/"+num) # add to jeer count
        ) 

    # obtain a random joke
    responses.append(
        requests.get(url+"/random")  # read a random joke
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")
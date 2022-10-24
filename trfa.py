from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_truefalse import *

app_api1 = Blueprint('apitf', __name__,
                   url_prefix='/api/trfa')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api1 = Api(app_api1)

class TrfaAPI:
    # not implemented
    class _Create(Resource):
        def post(self, trfa):
            pass
            
    # getJokes()
    class _Read(Resource):
        def get(self):
            return jsonify(getTrfas())

    # getJoke(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getTrfa(id))

    # getRandomJoke()
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomTrfa())
    
    # getRandomJoke()
    class _ReadCount(Resource):
        def get(self):
            count = countTrfa()
            countMsg = {'count': count}
            return jsonify(countMsg)

    # put method: addJokeHaHa
    class _UpdateLike(Resource):
        def put(self, id):
            addTrfaTrue(id)
            return jsonify(getTrfa(id))

    # put method: addJokeBooHoo
    class _UpdateJeer(Resource):
        def put(self, id):
            addTrfaFalse(id)
            return jsonify(getTrfa(id))

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api1.add_resource(_Create, '/create/<string:trfa>')
    api1.add_resource(_Read, '/')
    api1.add_resource(_ReadID, '/<int:id>')
    api1.add_resource(_ReadRandom, '/random')
    api1.add_resource(_ReadCount, '/count')
    api1.add_resource(_UpdateLike, '/like/<int:id>')
    api1.add_resource(_UpdateJeer, '/worst/<int:id>')
    
if __name__ == "__main__": 
    server = "http://127.0.0.1:5000" # run local
    # server = 'https://flask.nighthawkcodingsociety.com' # run from web
    url = server + "/api/trfa"
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
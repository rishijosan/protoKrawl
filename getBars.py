'''
Created on Apr 12, 2014

@author: Rishi Josan
'''

from flask import Flask
from flask import request, jsonify
import foursquare
import json

loc = '/media/sf_G_DRIVE/sharedWorkspace/protoKrawl/json/'

app = Flask(__name__)

#client = foursquare.Foursquare(client_id='ETWY3CHBMEFXU2DZZZ1DKTO2YPMNKJWNZTVSKBABBXTQEDW2', client_secret='X0H2FBGJ53ANMC23YHWQKI0LV5I52F12MWZMF5002EOJ0NSR', redirect_uri='http://127.0.0.1:5000/')



@app.route("/")
def hello():
    return "Hello World!"

@app.route("/getVenue" , methods=["GET", "POST"])
def getVenue():
    
    if request.method == "GET":
        
        #reqParams = request.get_json()
        reqParams = request.args
        lat = reqParams['lat']
        lon = reqParams['lon']
        #print str(lat+', '+lon)
    
        client = foursquare.Foursquare(client_id='ETWY3CHBMEFXU2DZZZ1DKTO2YPMNKJWNZTVSKBABBXTQEDW2', client_secret='X0H2FBGJ53ANMC23YHWQKI0LV5I52F12MWZMF5002EOJ0NSR')
        srch = client.venues.explore(params={'ll': str(lat+', '+lon), 'section' : 'drinks' , 'limit' : 10 })
        locations = srch['groups'][0]['items']
    
        locList = dict()
        n=0
        for item in locations:
            locList[n]=item['venue']
            n+=1
            
        #result = json.dumps(locList)
        return jsonify(locList)
    

if __name__ == "__main__":
    #app.debug = True
    app.run()

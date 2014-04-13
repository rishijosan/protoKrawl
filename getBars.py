'''
Created on Apr 12, 2014

@author: Rishi Josan
'''

from flask import Flask
import foursquare
import json

loc = '/media/sf_G_DRIVE/sharedWorkspace/protoKrawl/json/'

app = Flask(__name__)

#client = foursquare.Foursquare(client_id='ETWY3CHBMEFXU2DZZZ1DKTO2YPMNKJWNZTVSKBABBXTQEDW2', client_secret='X0H2FBGJ53ANMC23YHWQKI0LV5I52F12MWZMF5002EOJ0NSR', redirect_uri='http://127.0.0.1:5000/')



@app.route("/")
def hello():
    return "Hello World!"

@app.route("/getVenue")
def getVenue():
    client = foursquare.Foursquare(client_id='ETWY3CHBMEFXU2DZZZ1DKTO2YPMNKJWNZTVSKBABBXTQEDW2', client_secret='X0H2FBGJ53ANMC23YHWQKI0LV5I52F12MWZMF5002EOJ0NSR')
    ven  = client.venues('40a55d80f964a52020f31ee3')
    srch = client.venues.search(ll='40.7,-74')
    print srch
    lat = 40.7
    long = -74
    
    with open(srch + 'srch.json', 'w') as outfile:
        json.dump(ven, outfile)
        
    return "Venue Dumped"
    

if __name__ == "__main__":
    #app.debug = True
    app.run()

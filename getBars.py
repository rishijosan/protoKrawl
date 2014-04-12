'''
Created on Apr 12, 2014

@author: Rishi Josan
'''

from flask import Flask
import foursquare
import json

app = Flask(__name__)

#client = foursquare.Foursquare(client_id='ETWY3CHBMEFXU2DZZZ1DKTO2YPMNKJWNZTVSKBABBXTQEDW2', client_secret='X0H2FBGJ53ANMC23YHWQKI0LV5I52F12MWZMF5002EOJ0NSR', redirect_uri='http://127.0.0.1:5000/')



@app.route("/")
def hello():
#===============================================================================
#    auth_uri = client.oauth.auth_url()
#    # Interrogate foursquare's servers to get the user's access_token
#    access_token = client.oauth.get_token(auth_uri)
# 
#    # Apply the returned access token to the client
#    client.set_access_token(access_token)
# 
#    # Get the user's data
#    user = client.users()
#===============================================================================

    client = foursquare.Foursquare(client_id='ETWY3CHBMEFXU2DZZZ1DKTO2YPMNKJWNZTVSKBABBXTQEDW2', client_secret='X0H2FBGJ53ANMC23YHWQKI0LV5I52F12MWZMF5002EOJ0NSR')
    ven  = client.venues('40a55d80f964a52020f31ee3')
    print ven
    with open('/media/sf_G_DRIVE/data.txt', 'w') as outfile:
        json.dump(ven, outfile)
    return "Hello World!"

if __name__ == "__main__":
    app.run()

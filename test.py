'''
Created on Apr 12, 2014

@author: root
'''

import foursquare
import json
loc = '/media/sf_G_DRIVE/sharedWorkspace/protoKrawl/json/'

client = foursquare.Foursquare(client_id='ETWY3CHBMEFXU2DZZZ1DKTO2YPMNKJWNZTVSKBABBXTQEDW2', client_secret='X0H2FBGJ53ANMC23YHWQKI0LV5I52F12MWZMF5002EOJ0NSR')
srch = client.venues.search(params={'ll': '40.7,-74'})
#srch = client.venues.search(params={'query': 'coffee'})
print srch
    
with open(loc+'/srch.json', 'w') as outfile:
    json.dump(srch, outfile)
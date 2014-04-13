'''
Created on Apr 12, 2014

@author: root
'''

import foursquare
import json
loc = '/home/rishi/'

client = foursquare.Foursquare(client_id='ETWY3CHBMEFXU2DZZZ1DKTO2YPMNKJWNZTVSKBABBXTQEDW2', client_secret='X0H2FBGJ53ANMC23YHWQKI0LV5I52F12MWZMF5002EOJ0NSR')
#srch = client.venues.search(params={'ll': '40.5212735, -74.4567546' , 'categoryId': '4d4b7105d754a06376d81259' , 'limit' : 10, 'radius' : 5000})
#srch = client.venues.search(params={'query': 'coffee'})
#srch = client.venues.search(params={'near': 'Stony Brook'})
#srch = client.venues.explore(params={'ll': '40.5212735, -74.4567546', 'limit' : 100, 'price' : [1,2,3] , 'day' : 6, })
#srch = client.venues.explore(params={'ll': '40.5212735, -74.4567546', 'section' : 'drinks' , 'limit' : 10, 'price' : [1,2,3] , 'day' : 6 })

srch = client.venues.explore(params={'ll': '40.5212735, -74.4567546', 'section' : 'drinks' , 'limit' : 10 })
locations = srch['groups'][0]['items']

locList = dict()
n=0
for item in locations:
    locList[n]=item['venue']
    n+=1
    
result = json.dumps(locList)
print srch

    
with open(loc+'drinks30.json', 'w') as outfile:
    json.dump(srch, outfile)
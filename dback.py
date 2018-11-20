import json
import requests
# import all for websocket
import socket

class ConnectData():

    def __init__(self):
        self.url = 'http://localhost:3000/api/v1/'

    def getData(self, arg):
        response = requests.get(self.url+arg)
        if response.status_code == 200 :
             print(response.content)

             pass

        else:
            print(response.status_code)

co = ConnectData()
co.getData('indicators/1')

local = socket.socket()

local.bind(('', 5000))
local.listen(1)
print('hey')
while True :
    print 'accept'
    c, addr = local.accept()
    print 'Got connection from '+ addr
    c.send('Connecting to Back-End')

c.close()

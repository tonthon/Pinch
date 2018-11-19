import json
import requests

class ConnectData():

    def __init__(self, arg):

        self.url = 'http://localhost:3000/api/v1/' + arg
        response = requests.get(self.url)

        if response.status_code == 200 :
             print(response.content)
             print("connect")
             pass

        else:
            print('no')
            print(response.status_code)

ConnectData('indicators/3')

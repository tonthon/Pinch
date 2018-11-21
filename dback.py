import json
import requests
import pprint
import os
# import all for websocket
import socket
import inotify, inotify.adapters

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
# co.getData('indicators/1')

def _main():
    i = inotify.adapters.Inotify()
    # set file to watch
    url = os.getcwd()+'/db.json'
    i.add_watch(url)

    with open(url, 'r'):
        pass


    events = i.event_gen(yield_nones=False, timeout_s=1)
    events = list(events)
    # pprint.pprint(events)
    print 'call more info'
    pprint.pprint(events)


_main()

# socket part
# local = socket.socket()
# local.bind(('', 5050))
# local.listen(1)
# print('hey')
# while True :
#     print 'accept'
#     c, addr = local.accept()
#     print 'Got connection from '
#     print addr
#     c.send('Connecting to Back-End')
# c.close()

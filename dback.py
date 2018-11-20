import json
import requests
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

    i.add_watch('/tmp')

    with open('/tmp/db.json', 'w'):
        pass

    events = i.event_gen(yield_nones=False, timeout_s=1)
    events = list(events)
    print(events)


_main()

# def _watchIno():
#     i = inotify.adapters.Inotify()
#     i.add_watch('/')
#
#     with open('db.json', 'w'):
#         pass
#
#
#     events = i.event_gen(yield_nones=False, timeout_s=1)
#     events = list(events)
#     print(events)
#
#
# _watchIno()
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

import json
import requests
import pprint
import os
# import all for websocket
import asyncio
import websockets
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

def _main():
    i = inotify.adapters.Inotify()
    # set file to watch
    url = os.getcwd()+'/db.json'
    i.add_watch(url)

    with open(url, 'r'):
        pass
    # for event in i.event_gen(yield_nones=False):
    #     (_, type_names, path, filename) = event
    #
    #     print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
    #           path, filename, type_names))
    events = i.event_gen(yield_nones=False, timeout_s=1)
    events = list(events)
    return events

pprint.pprint(_main())

async def testws(websocket, path):
    event = _main()
    while event :#event inotify:

        await websocket.send(event)


startserver = websockets.serve(testws, 'localhost', 5432)
pprint.pprint(startserver)
asyncio.get_event_loop().run_until_complete(startserver)
asyncio.get_event_loop().run_forever()

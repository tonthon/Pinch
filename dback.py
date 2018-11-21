import os
import asyncio
import websockets
import inotify, inotify.adapters


async def testws(websocket, path):
    """
    Écoute les modifications sur le fichier db.json et transmets le nom du
    fichier modifié au travers de la websocket

    :param obj websocket: La websocket
    :param str path: L'url utilisée par la websocket
    """
    i = inotify.adapters.Inotify()
    # On définit le fichier à observer
    url = os.getcwd()+'/db.json'
    i.add_watch(url)

    for event in i.event_gen(yield_nones=False):
        # Si on fait un touch on reçoit des évènements ici
        print("We've got an event from inotify")
        print(event)
        event, event_type, filepath, filename = event
        # On envoie le chemin vers le fichier ici
        await websocket.send(filepath)


def launch_server():
    startserver = websockets.serve(testws, 'localhost', 5432)
    asyncio.get_event_loop().run_until_complete(startserver)
    asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    launch_server()

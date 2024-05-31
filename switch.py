#!/usr/bin/env python3

import sys
import time


sys.path.append('../')
from obswebsocket import obsws, requests  # noqa: E402

host = "localhost"
port = 4455
password = "5sgHKzbOQIzW4ixT"

def switch(scenename):
    ws = obsws(host, port, password)
    ws.connect()

    try:
        scenes = ws.call(requests.GetSceneList())
        for s in scenes.getScenes():
            name = scenename
            print("Switching to {}".format(name))
            ws.call(requests.SetCurrentProgramScene(sceneName=name))
            time.sleep(2)

        print("End of list")

    except KeyboardInterrupt:
        pass

    ws.disconnect()

switch("Scene2")
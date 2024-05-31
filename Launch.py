import obsws_python as obs
import time
import subprocess
import os
# Define connection details (update as needed)

os.chdir("C:\\Program Files\\obs-studio\\bin\\64bit")
subprocess.Popen(["C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"])
time.sleep(10)
host = 'localhost'
port = 4455
password = '5UsvT80aANE10yuL'
timeout = 3

# Create a request client
client = obs.ReqClient(host=host, port=port, password=password, timeout=timeout)

# Open a fullscreen projector for a specific scene
printname=client.send("GetCurrentProgramScene",raw=True)
scene_name = printname["sceneName"]  # Replace with your scene name
monitor_index = 1  # Monitor index, 0 for primary monitor, 1 for secondary, etc.

# Send request to open fullscreen projector
response = client.send('OpenVideoMixProjector', {
    'videoMixType': "OBS_WEBSOCKET_VIDEO_MIX_TYPE_PREVIEW",
    'monitorIndex': monitor_index
})

time.sleep(3)


print(f"Fullscreen projector opened for scene '{scene_name}' on monitor {monitor_index}.")
print(printname)



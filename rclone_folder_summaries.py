import subprocess as sp
import os
import json


folder_list = json.loads(open("root_folders.json","r").read())

def run_file_search(gdir):
  existing = os.listdir("./")
  for e in existing:
    if gdir in e:
      print("already ran ",gdir," quitting")
      return
  cmd = f'rclone lsjson -R --files-only baylyd:"/{gdir}" > "{gdir}".json'
  sp.run(cmd,shell=True)

for folder in folder_list:
  print("running",folder)
  run_file_search(folder["Path"])



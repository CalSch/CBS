#!/usr/bin/env python3
from sys import argv
import os
import json
import requests



version=1

# def check_for_updates():
    # latest=requests.get()

usage="""usage: cbs post|setup [TEXT]

actions:
  post TEXT: make a post with TEXT as content
  setup: setup CBS 
"""

conf_file=f'{os.environ.get("HOME")}/.cbs.conf'

if len(argv)<2:
    if not os.path.exists(conf_file):
        print("CBS has not been setup. Run 'cbs setup' to set it up.")
        quit()
    else:
        print(usage)
        quit()

action=argv[1]
if action=="setup":
    print("Setting up CBS...")
    # open('~/.cbs.conf','w+').close()
    with open(conf_file,'w') as f:
        data={
            "name": input("What should your username be? "),
            "server": input("What billboard server are you connecting to? ")
        }
        f.write(json.dumps(data))

if not os.path.exists(conf_file):
    print("CBS has not been setup. Run 'cbs setup' to set it up.")
    quit()

data=""
with open(conf_file,'r') as f:
    data=json.loads(f.read())
if action=="post":
    if len(argv)>3:
        print("Too many arguments. Please wrap the post content in quotes.")
        quit()
    text=argv[2]
    name=data['name']
    res=requests.post(f'http://{data["server"]}/post',{"text":text,"name":name})
    if res.status_code == 403:
        print("403 error. dont know what broke but thats not supposed to happen.")
    elif res.status_code == 200:
        print("Post sent :)")
    else:
        print(f"I have no idea what went wrong, heres the status code: {res.status_code}")
    

    
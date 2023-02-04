import json
import os

import requests

url = "https://api.storyblok.com/v2/cdn/stories/"

querystring = {"token": "X6ZB3Mf85AtoI3Esc8EH4gtt"}

payload = ""
headers = {}

response = requests.request(
    "GET", url, data=payload, headers=headers, params=querystring)
json_object = json.loads(response.text)
print(json_object["stories"])


# {"parent_folder": ["child_1", "child_2"]}
def createFolders(fullPath: dict):
    items = fullPath.items()
    for parentFolder, childFolders in items:
        for childFolder in childFolders:
            os.makedirs(os.path.join(parentFolder, childFolder))


# {"key", "value"} => {"fileNameWithDir": "code"}
def createCode(fileInput: dict):
    for fileNameWithDir, code in fileInput.items():
        with open(fileNameWithDir, 'w') as file:
            file.write(code)


if __name__ == '__main__':
    # print('Running...')
    # createFolders({"parent_folder": ["child_1", "child_2"], "parent_folder/child_1": [
    #               "child_1_2", "child_2_1"]})
    # createCode({'test/demo.py': 'print("Hello World")'})
    for i in range(len(json_object["stories"])):
        current_story = json_object["stories"][i]["content"]
        fullPath = eval(current_story["folders"])
        fileInput = eval(current_story["code"])
        createFolders(fullPath)
        createCode(fileInput)

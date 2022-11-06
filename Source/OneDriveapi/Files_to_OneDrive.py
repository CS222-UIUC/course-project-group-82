import os
import requests
from OneDriveAccess import generate_access_token, GRAPH_API_ENDPOINT

APP_ID = '9a0921a7-905e-481a-ab14-a1a75f4d2a8f'
SCOPES = ['Files.ReadWrite']

access_token = generate_access_token(APP_ID, SCOPES)
headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}

file_path = r'/Users/alexisserrano/Documents/CS222_82/course-project-group-82/Source/images/IMG_1217.png'
file_name = os.path.basename(file_path)
with open(file_path, 'rb') as upload:
    media_content = upload.read()

#Upload file to home directory
response = requests.put(
    GRAPH_API_ENDPOINT + f'/me/drive/items/root:/{file_name}:/content',
    headers=headers, 
    data=media_content
)




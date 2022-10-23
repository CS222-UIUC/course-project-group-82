import os
import requests
from OneDriveAccess import generate_access_token, GRAPH_API_ENDPOINT

APP_ID = ''
SCOPES = ['Files.ReadWrite']

access_token = generate_access_token(APP_ID, SCOPES)
headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}

file_path = ''
with open(file_path, 'rb') as upload:
    media_content = upload.read()





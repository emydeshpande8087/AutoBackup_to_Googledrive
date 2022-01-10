from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from pathlib import Path
import os.path
store_keys_path=Path('stored_keys')

def coldstart():
    '''Function to create an instance of your Drive
    Input : None
    Output: drive object'''
    # Setup the Drive v3 API
    SCOPES = 'https://www.googleapis.com/auth/drive.file'
    key_path=str(os.path.join(store_keys_path,'credentials.json'))
    #store = file.Storage('credentials.json')  # fetches single credentials
    store = file.Storage(key_path)  # fetches single credentials
    creds = store.get()
    print('Retrieving credentials ... No need to re-authenticate :) ')
    if not creds or creds.invalid:
        print('Initial Authentication ! \n Please allow the access for this app to your Google Drive')
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    google_drive_service = build('drive', 'v3', http=creds.authorize(Http()))
    return google_drive_service

import pprint

from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

folder_id = None


def createFolderForAllUploads(google_drive_service):
    file_metadata = {
        'name': 'Auto Uploading Bot',
        'mimeType': 'application/vnd.google-apps.folder'
    }
    # Create the folder using drive service object
    file = google_drive_service.files().create(body=file_metadata, fields='id').execute()
    print('Auto uploading Folder id is : ', file.get('id'))


def checkIfAutoFolderExists(service):
    response=service.files().list().execute()
    pprint.pprint(response)
    relist=response.get('files')[0]
    print('=========================')
    pprint.pprint(relist['id'])
    pprint.pprint(relist['name'])



def uploadFile(google_drive_service):
    # Create File metadata object
    file_metadata = {
        'name': 'boss.txt',
        'parents': [folder_id]
    }
    # Create media file upload object with resumable upload and download
    media = MediaFileUpload('boss.txt',
                            mimetype='*/*',
                            resumable=True)
    file = google_drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print('File ID: ' + file.get('id'))

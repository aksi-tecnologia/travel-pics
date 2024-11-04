from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
import os

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
PARENT_FOLDER_ID = os.environ['PARENT_FOLDER_ID']
WIDTH = 300

class GDrive:
    """
    A class to interact with Google Drive.
    """
    def __init__(self):
        self.service = self.authenticate()

    def authenticate(self):
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('drive', 'v3', credentials=creds)
        return service

    def make_public(self, file_id):
        """
        Make a file public.
        params:
            file_id: str
        returns:
            response: dict
        """
        request = self.service.permissions().create(fileId=file_id, body={'role': 'reader', 'type': 'anyone'})
        response = request.execute()
        return response

    def upload_file(self, file_path, parent_folder_id=PARENT_FOLDER_ID, public=False):
        """
        Upload a file to Google Drive.
        params:
            file_path: str
            public: bool (default=False) if True, the file will be made public
        returns:
            response: dict
        """
        file_metadata = {'name': file_path, 'parents': [parent_folder_id]}
        media = MediaFileUpload(file_path, resumable=True)
        request = self.service.files().create(body=file_metadata, media_body=media, fields='id')
        response = request.execute()
        if public:
            self.make_public(response['id'])
        return response
    
    def create_folder(self, folder_name):
        """
        Create a folder in Google Drive.
        params:
            folder_name: str
        returns:
            response: dict
        """
        file_metadata = {'name': folder_name, 'parents': [PARENT_FOLDER_ID], 'mimeType': 'application/vnd.google-apps.folder'}
        request = self.service.files().create(body=file_metadata, fields='id')
        response = request.execute()
        return response
    
    def list_files(self, parent_folder_id=PARENT_FOLDER_ID, page_size=100):
        """
        List all files in a folder.
        params:
            parent_folder_id: str (default=PARENT_FOLDER_ID)
        returns:
            response: dict
        """
        query = f"'{parent_folder_id}' in parents"
        request = self.service.files().list(pageSize=page_size, fields='nextPageToken, files(id, name, mimeType, webViewLink, thumbnailLink, size, modifiedTime, trashed)', q=query)
        response = request.execute()
        return response
    
    def delete_file(self, file_id):
        """
        Delete a file.
        """
        request = self.service.files().delete(fileId=file_id)
        response = request.execute()
        return response
    
    def get_thumbnail(self, file_id, width=WIDTH):
        """
        Get a thumbnail of a file.
        params:
            file_id: str
            width: int (default=300)
        returns:
            url: str
        """
        url = f"https://lh3.google.com/u/0/d/{file_id}=w{width}"
        return url

if __name__ == '__main__':
    gdrive = GDrive()
    response = gdrive.upload_file('logo.png', parent_folder_id='1ZVz-fN5Z_u50ICiN74c_oiTUSaBGy29j', public=True)
    url = gdrive.get_thumbnail(response['id'], width=WIDTH)
    print(url)

    # response = gdrive.create_folder('teste')
    # print(response)

    response = gdrive.list_files(parent_folder_id='1ZVz-fN5Z_u50ICiN74c_oiTUSaBGy29j')
    print(response)



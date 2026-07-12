from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_credentials():
    flow = InstalledAppFlow.from_client_secrets_file('client_secret_446726219308-tc7f4h44blckbm2lr79seq80o2de3fie.apps.googleusercontent.com.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds

def list_files_in_folder(folder_id):
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)

    query = f"'{folder_id}' in parents"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get('files', [])

    for file in files:
        print(f"{file['name']} ({file['id']})")

if __name__ == '__main__':
    folder_id = '1_qiXrYL8UeYKzVn-P-5eNMoZbLPNJS6Q'
    list_files_in_folder(folder_id)

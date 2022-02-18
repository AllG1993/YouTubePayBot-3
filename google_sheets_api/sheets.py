import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'ytpb-3-test-creds.json'


class TableProcessor:
    def __init__(self, credentials_file):
        self.credentials_file = credentials_file
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file,
                                                                       ['https://www.googleapis.com/auth/spreadsheets',
                                                                        'https://www.googleapis.com/auth/drive'])
        self.http_auth = credentials.authorize(httplib2.Http())
        self.service = apiclient.discovery.build('sheets', 'v4', http=self.http_auth)

    def create_table(self, new_table_name: str, sheet_name_in_table: str, row_count: int, column_count: int):
        spreadsheet = self.service.spreadsheets().create(body={
            'properties': {'title': new_table_name, 'locale': 'ru_RU'},
            'sheets': [{'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': sheet_name_in_table,
                'gridProperties': {'rowCount': row_count, 'columnCount': column_count}
            }}]
        }).execute()
        return {'spreadsheet_id': spreadsheet['spreadsheetId'], 'spreadsheet_url': spreadsheet['spreadsheetUrl']}

    def table_access(self, spreadsheet_id, gmail_address, role):
        drive_service = apiclient.discovery.build('drive', 'v3',
                                                  http=self.http_auth)  # Выбираем работу с Google Drive и 3 версию API
        access = drive_service.permissions().create(
            fileId=spreadsheet_id,
            body={'type': 'user', 'role': role, 'emailAddress': gmail_address},
            fields='id'
        ).execute()


if __name__ == '__main__':
    ...
    # gh_w_1 = TableProcessor(CREDENTIALS_FILE)
    # t_1 = gh_w_1.create_table('t1', 'list_1', 100, 10)
    # gh_w_1.table_access(t_1['spreadsheet_id'], 'alekseygalkovich@gmail.com', 'writer')
    # print(t_1['spreadsheet_url'])



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
        """
        Создает гугл таблицу в которой:
        :param new_table_name: Имя новой таблицы
        :param sheet_name_in_table: Имя листа в таблице
        :param row_count: Количество строк в таблице
        :param column_count: количество колонок в таблице
        :return: Словарь, где spreadsheet_id - это ID созданной таблицы, а spreadsheet_url - это ссылка на нее.
        """
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

    def access_table(self, spreadsheet_id, gmail_address, role):
        """
        Дает пользователю права на таблицу
        :param spreadsheet_id: ID таблицы к которой даем доступ
        :param gmail_address: Gmail пользователя
        :param role: роль: owner, organizer, fileOrganizer, writer, commenter, reader
        :return:
        """
        drive_service = apiclient.discovery.build('drive', 'v3',
                                                  http=self.http_auth)  # Выбираем работу с Google Drive и 3 версию API
        access = drive_service.permissions().create(
            fileId=spreadsheet_id,
            body={'type': 'user', 'role': role, 'emailAddress': gmail_address},
            fields='id'
        ).execute()

    def append_table(self, values: list, spreadsheet_id: str, sheet_name: str, value_input_option=0):
        """
        Дозаписывает данные в следующую свободную строку таблицы.
        :param values: Список списков с данными, где каждый список в списке это одна строка в таблице.
        :param spreadsheet_id: ID таблицы в которую будут дозаписаны данные.
        :param sheet_name: Имя листа в который будем дозаписывать данные.
        :param value_input_option: Метод записи, сде 0 - это RAW, то есть сырая строка, а 1 - это USER_ENTERED,
        означает что будет распознано как ввод пользователем и к этим данным будут применяться формулы и с ними,
        будут производиться вычисления.
        :return:
        """
        body = {
            'values': values
        }

        result = self.service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            body=body, range=sheet_name,
            valueInputOption=['RAW', 'USER_ENTERED'][value_input_option]
        ).execute()
        return result['updates']['updatedRange']


if __name__ == '__main__':
    gh_w_1 = TableProcessor(CREDENTIALS_FILE)
    # t_1 = gh_w_1.create_table('t1', 'list_1', 100, 10)
    # gh_w_1.access_table('11Uon-RJ_NahW-hAJiCb78zhstKOUDRw6nh_4hL9XI4A', 'alekseygalkovich@gmail.com', 'writer')
    # print(gh_w_1)
    print(gh_w_1.append_table([['=2*5', '2', '3']], '11Uon-RJ_NahW-hAJiCb78zhstKOUDRw6nh_4hL9XI4A', 'list_1'))



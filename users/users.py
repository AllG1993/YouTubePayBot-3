import os
from pathlib import Path

import google_sheets_api
from google_sheets_api.sheets import SpreadsheetProcessor


creds_path = Path(Path.cwd().parent, 'ytpb-3-test-creds.json')


class User:
    def __init__(self, tg_user_id, spreadsheet_handler):
        self.tg_user_id = tg_user_id
        self.users_list = spreadsheet_handler.read_table('users!A2:I')

        self.trusted_user = False
        self.id = None
        self.name = None
        self.role = False

        for user in self.users_list:
            if self.tg_user_id == int(user[0]):
                self.trusted_user = True
                self.id = int(user[0])
                self.name = user[1]
                self.role = user[2]


if __name__ == '__main__':
    gs_handler = SpreadsheetProcessor(creds_path, '11Uon-RJ_NahW-hAJiCb78zhstKOUDRw6nh_4hL9XI4A')
    user_1 = User(374783606, gs_handler)
    print(user_1.trusted_user)
    print(user_1.role)
    print(user_1.name)
    print(user_1.id)
    user_2 = User(590910946, gs_handler)
    print(user_2.trusted_user)
    print(user_2.role)
    print(user_2.name)
    print(user_2.id)
    print(google_sheets_api.ppp)
    # print(type(user_1.users_list))
    # print(True if user_1.tg_user_id in user_1.users_list[0] else False)

    ...



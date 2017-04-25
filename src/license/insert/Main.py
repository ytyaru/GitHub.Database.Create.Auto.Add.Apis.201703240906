#!python3
#encoding:utf-8
import os.path
import subprocess
import license.insert.Data
import license.insert.command.miscellaneous.Licenses
class Main:
    def __init__(self, user_name, path_db_account, path_db_repo, path_db_license):
        self.data = license.insert.Data.Data(user_name, path_db_account, path_db_repo, path_db_license)
        self.licenses = license.insert.command.miscellaneous.Licenses.Licenses(self.data)

    def Initialize(self):
        self.__InsertForFile()

    def Run(self):
        license_key = 'start'
        while '' != license_key:
            print('入力したKeyのライセンスを問い合わせます。(未入力+Enterで終了)')
            print('サブコマンド    l:既存リポジトリ m:一覧更新  f:ファイルから1件ずつ挿入')
            key = input()
            if '' == key:
                break
            elif 'l' == key or 'L' == key:
                self.licenses.Show()
            elif 'f' == key or 'F' == key:
                self.__InsertForFile()
            elif 'm' == key or 'M' == key:
                self.licenses.Update()
            else:
                self.licenses.InsertOne(key)

    def __InsertForFile(self):
        file_name = 'LicenseKeys.txt'
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
        if not(os.path.isfile(file_path)):
            print(file_name + 'ファイルを作成し、1行ずつキー名を書いてください。')
            return
        with open(file_path, mode='r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())
                self.licenses.InsertOne(line.strip())


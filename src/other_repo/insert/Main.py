#!python3
#encoding:utf-8
import os.path
import getpass
import other_repo.insert.Data
import other_repo.insert.command.repositories.Inserter
class Main:
    def __init__(self, user_name, path_db_account, path_db_other_repo, path_db_license):
        self.data = other_repo.insert.Data.Data(user_name, path_db_account, path_db_other_repo, path_db_license)
        self.inserter = other_repo.insert.command.repositories.Inserter.Inserter(self.data)
        
    def Initialize(self):
        path_this_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(path_this_dir, "OtherRepositoryUrl.txt")
        with open(file_path, mode="r", encoding="utf-8") as f:
            url = True
            while url:
                url = f.readline().rstrip('\r\n')
                print(url)
                if len(url) == 0:
                    continue
                username = self.data.get_other_username(url)
                repo_name = self.data.get_other_repo_name(url)
                print("ユーザ名: " + username)
                print("リポジトリ名: " + repo_name)
                self.inserter.Insert(username, repo_name)
        
    def Run(self):
        print('GitHubリポジトリ情報を取得します。')
        url = 'start'
        while '' != url:
            print('GitHubリポジトリのURLを入力してください。(未入力+Enterで終了)')
            print('サブコマンド    l:既存リポジトリ')
            url = input()
            if '' == url:
                break
            elif 'l' == url or 'L' == url:
                self.inserter.Show()
            else:
                username = self.data.get_other_username(url)
                repo_name = self.data.get_other_repo_name(url)
                print("ユーザ名: " + username)
                print("リポジトリ名: " + repo_name)
                # 未登録ならDBへ挿入する（GitHubAPIでリポジトリ情報、言語情報、ライセンス情報を取得して）
                self.inserter.Insert(username, repo_name)


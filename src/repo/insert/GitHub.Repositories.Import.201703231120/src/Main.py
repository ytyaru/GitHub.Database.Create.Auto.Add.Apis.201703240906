from github import GitHub
import json
import github.db.repositories.LanguagesAggregate

class Main(object):
    def __init__(self):
        pass
    def Run(self):
        github_user_name = 'ytyaru'
        os_user_name = getpass.getuser()
        device_name = '85f78c06-a96e-4020-ac36-9419b7e456db'
        path_db_base = 'mint/root/db/Account/GitHub'
        path_db_license = '/media/{0}/{1}/{2}/private/v0/GitHub.Licenses.sqlite3'.format(os_user_name, device_name, path_db_base)
        path_db_api = "/media/{0}/{1}/{2}/public/v0/GitHub.Apis.sqlite3".format(os_user_name, device_name, path_db_base)
        path_db_account = '/media/{0}/{1}/{2}/private/v0/GitHub.Accounts.sqlite3'.format(os_user_name, device_name, path_db_base)
#        path_db_repo = '/media/{0}/{1}/{2}/public/v0/GitHub.Repositories.{3}.sqlite3'.format(os_user_name, device_name, path_db_base, github_user_name)
        path_db_repo = './GitHub.Repositories.{3}.sqlite3'.format(github_user_name)

        g = GitHub.GitHub(path_db_account, path_db_api, path_db_repo, github_user_name)
        res = g.db.update_local_db()

        aggr = github.db.repositories.LanguagesAggregate.LanguagesAggregate(db_path_repo)
        aggr.show()


if __name__ == "__main__":
    m = Main()
    m.Run()


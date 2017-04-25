#!python3
#encoding:utf-8
from github.api import RequestParam
from github.api.repositories import Repositories
import github.db.repositories.Repositories
class GitHub:
    def __init__(self, db_path_account, db_path_api, db_path_repo, username):
        self.req = RequestParam.RequestParam(db_path_account, db_path_api, username)
        self.repo = Repositories.Repositories(self.req)
        self.db = github.db.repositories.Repositories.Repositories(db_path_repo, self.req)

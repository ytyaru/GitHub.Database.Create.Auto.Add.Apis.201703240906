#!python3
#encoding:utf-8
import dataset
import requests
import urllib.parse
import datetime
import time
import pytz
import json
import github.api.Pagenation
import github.db.repositories.Languages
class Repositories:
    def __init__(self, db_path_repo, req_param):
        self.req = req_param
        self.db_path_repo = db_path_repo
        self.db_repo = dataset.connect('sqlite:///' + db_path_repo)
        self.page = github.api.Pagenation.Pagenation(req_param)
        self.lang = github.db.repositories.Languages.Languages(db_path_repo, req_param)
    def update_local_db(self):
        now = datetime.datetime.now(pytz.utc)
        diff_repos = self.__get_repos_diff()
        self.db_repo.begin()
        for r in diff_repos:
            self.db_repo['Repositories'].insert(dict(
                IdOnGitHub=r['id'],
                Name=r['name'],
                Description=r['description'],
                Homepage=r['homepage'],
                CreatedAt=r['created_at'],
                PushedAt=r['pushed_at'],
                UpdatedAt=r['updated_at'],
                CheckedAt="{0:%Y-%m-%dT%H:%M:%SZ}".format(now)))
            repo = self.db['Repositories'].find_one(IdOnGitHub=r['id'])
            self.db_repo['Counts'].insert(dict(
                RepositoryId=repo['Id'],
                Forks=r['forks_count'],
                Stargazers=r['stargazers_count'],
                Watchers=r['watchers_count'],
                Issues=r['open_issues_count']))
        self.db_repo.commit()
#        self.lang.update_local_db()
        return diff_repos

    def __get_repos_diff(self):
        since = self.__get_since_repo_id()
        print(since)
        method = 'GET'
        endpoint = 'user/repos'
        params = self.req.get(method, endpoint)
        params['params'] = {"type": "all", "sort": "created", "direction": "desc", "per_page": 100}
        r = requests.get(urllib.parse.urljoin("https://api.github.com", endpoint), **params)
        res = None
        if since is None:
            res = self.page.pagenate(r, r.json())
        else:
            res = self.__pagenate(r, r.json(), since)
        res.reverse()
        return res

    """
    指定したリポジトリIDよりも新しいリポジトリだけをすべて返す。
    @param [requests.response] r is response object.
    @param [json] res is json object.
    @param [int] since is github repository id.
    @param [int] start is github repositories index.
    """
    def __pagenate(self, r, res, since, start=0):
        print("since={0}".format(since))
        count = 0
        for repo in res[start:]:
            print("{0} {1}".format(repo['id'], repo['name']))
            if not(since == repo['id']):
                count = count + 1
            else:
                break
        start += count
        # 存在しないなら(このページはすべて返すべき対象。次ページにも対象がある可能性がある)
        if count == len(res):
            print("num {0}".format(len(res)))
            print(r.links)
            if "next" in r.links.keys():
                print(r.links["next"]["url"])
                params = self.req.update_otp()
                if "params" in params:
                    del params["params"]
                r2 = requests.get(r.links["next"]["url"], **params)
                res += r2.json()
                print("  num {0}".format(len(r2.json())))
                print("sum num {0}".format(len(res)))
                time.sleep(2)
                return self.__pagenate(r2, res, since, (start + 1))
            else:
                print("all num {0}".format(len(res)))
                print("len(res[:start]) {0}".format(len(res[:start])))
                return res[:start]
        else:
            print("all num {0}".format(len(res)))
            print("len(res[:start]) {0}".format(len(res[:start])))
            return res[:start]

    def __get_since_repo_id(self):
        repo = self.db_repo['Repositories'].find_one(order_by='-CreatedAt')
        print(repo)
        if repo is None:
            return None
        else:
            return repo['IdOnGitHub']

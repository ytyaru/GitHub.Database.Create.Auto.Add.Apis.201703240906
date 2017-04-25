# このソフトウェアについて

指定したGitHubユーザの全リポジトリ情報を取得する。（言語ファイルサイズとライセンスも）

GitHub.Repo.Insert.20170127181431796ベース。

# 開発環境

* Windows XP Pro SP3 32bit
    * cmd.exe
* [Python 3.4.4](https://www.python.org/downloads/release/python-344/)
    * [requests](http://requests-docs-ja.readthedocs.io/en/latest/)
    * [dataset](https://github.com/pudo/dataset)
    * [furl](https://github.com/gruns/furl)

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 準備

## 必要なデータベースを作成する

* [GitHub.Accounts.Database](https://github.com/ytyaru/GitHub.Accounts.Database.20170107081237765)
    * [GiHubApi.Authorizations.Create](https://github.com/ytyaru/GiHubApi.Authorizations.Create.20170113141429500)
* [GitHub.ApiEndpoint.Database.Create](https://github.com/ytyaru/GitHub.ApiEndpoint.Database.Create.20170124085656531)
* [GitHub.Repositories.Database.Create](https://github.com/ytyaru/GitHub.Repositories.Database.Create.20170114123411296)

## パラメータ設定

`src/Main.py`にある以下の変数や引数を任意に設定する。

```python
username = "github_username"
db_path_account = "C:/GitHub.Accounts.sqlite3"
db_path_api = "C:/GitHub.Apis.sqlite3"
db_path_repo = "C:/GitHub.Repositories.{0}.sqlite3".format(username)

g = GitHub.GitHub(db_path_account, db_path_api, db_path_repo, username)
```

# 実行

```dosbatch
python Main.py
```

# 結果

リポジトリの情報をローカルDBに反映する。プログラミング言語とバイト数も取得し挿入する。その集計を表示する。

![img](https://cdn-ak.f.st-hatena.com/images/fotolife/y/ytyaru/20170127/20170127215635.png)

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

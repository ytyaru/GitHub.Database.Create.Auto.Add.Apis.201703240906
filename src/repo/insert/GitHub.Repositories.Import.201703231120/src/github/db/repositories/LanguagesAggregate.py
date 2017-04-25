#!python3
#encoding:utf-8
import dataset
from datetime import datetime
class LanguagesAggregate:
    def __init__(self, db_path_repo):
        self.db_repo = dataset.connect('sqlite:///' + db_path_repo)

    def show(self):
        format = '%Y-%m-%dT%H:%M:%SZ'
        days = (datetime.strptime(self.get_last_date(), format) - datetime.strptime(self.get_first_date(), format)).days
        print('FirstDate: {0}'.format(self.get_first_date()))
        print('LastDate:  {0}'.format(self.get_last_date()))
        print('{0} 日間'.format(days))
        print("all repos: {0}".format(self.get_all_repo_num()))
        print('{0} repo/日'.format(self.get_all_repo_num() / days))
        print('all size:  {0} Byte'.format(self.get_all_repo_size()))
        self.show_sizes_by_languages()

    def get_first_date(self):
        return self.db_repo.query('select min(CreatedAt) FirstDate from Repositories').next()['FirstDate']
    def get_last_date(self):
        return self.db_repo.query('select max(CreatedAt) LastDate from Repositories').next()['LastDate']

    def get_all_repo_num(self):
        return self.db_repo['Repositories'].count()

    def get_all_repo_size(self):
        return self.db_repo.query('select sum(Size) AllSize from Languages').next()['AllSize']

    def get_sizes_by_languages(self):
        lang_dict = {"names":[], "sizes":[]}
        for lang in self.db_repo.query('select Language, sum(Size) SumSize from Languages group by Language order by SumSize desc'):
            lang_dict["names"].append(lang['Language'])
            lang_dict["sizes"].append(lang['SumSize'])

    def show_sizes_by_languages(self):
        # 桁あわせ：最も長い言語名を取得する
        name_length = 0
        for res in self.db_repo.query('select * from Languages where length(Language)=(select max(length(Language)) from Languages)'):
            name_length = res['Language']

        # 桁あわせ：最も大きい言語別合計Byteを取得する
        size_length = self.db_repo.query('select sum(Size) SumSize from Languages group by Language order by SumSize desc').next()['SumSize']

        # 言語別の合計Byte数
        format_str = "  {0:<%d}: {1:>%d} Byte" % (len(name_length), len(str(size_length)))
        for lang in self.db_repo.query('select Language, sum(Size) SumSize from Languages group by Language order by SumSize desc'):
            print(format_str.format(lang['Language'], lang['SumSize']))

import pymongo
import pandas as pd


def to_csv_user():
    client = pymongo.MongoClient('localhost')
    cur = client["zhihu_user_network"]["users_info"]
    data = pd.DataFrame(list(cur.find()))
    del data["_id"]
    # 去除重复项
    data.drop_duplicates()
    # 存储的时候可以做一些数据清洗的工作,清洗脏数据
    data.to_csv("zhihu_user.csv")


if __name__ == '__main__':
    to_csv_user()
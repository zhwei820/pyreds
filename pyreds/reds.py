#!/usr/bin/env python
import re

from pyreds.rclient import create_client
from pyreds.reds_ch import Search as SearchCh, Query as QueryCh
from pyreds.reds_en import Search as SearchEn, Query as QueryEn

searchch = None
searchen = None


def create_search(key):
    if not key:
        raise ValueError('create_search() requires a redis key for namespacing.')

    global searchch, searchen
    if not searchch:
        searchch = SearchCh(key)
    if not searchen:
        searchen = SearchEn(key)

    return Search(key)


def check_contain_chinese(check_str):
    '''
    检查是否含有中文
    :param check_str:
    :return:
    '''
    for c in check_str:
        if '\u4e00' <= c <= '\u9fa5':
            return True
    return False


def split_en_from_ch(s):
    '''
    去除汉字,只保留英文
    :param s:
    :return:
    '''
    p = re.compile(r'[\u4e00-\u9fa5]')
    return ' '.join(p.split(s))


# Initialize a new `Search` with the given `key`.
class Search:

    def __init__(self, key):
        self.key = key
        self.client = create_client()

    # Index the given `str` mapped to `id`
    def index(self, txt, id):
        global searchch, searchen

        if check_contain_chinese(txt):
            searchen.index(split_en_from_ch(txt), id)  # todo 待优化
            return searchch.index(txt, id)
        else:
            return searchen.index(txt, id)

    # to remove index
    def remove(self, id):
        key = self.key
        db = self.client

        constants = db.zrevrangebyscore(key + ':object:' + str(id), '+inf', 0)

        pipe = db.pipeline()
        pipe.delete(key + ':object:' + str(id))

        for c in constants:
            pipe.zrem(key + ':word:' + c.decode('utf-8'), id)

        return pipe.execute()

    # Perform a search on the given `query` returning
    # a `Query` instance.
    def query(self, txt, type=None):
        global searchch, searchen

        if check_contain_chinese(txt):
            return QueryCh(txt, type, searchch)
        else:
            return QueryEn(txt, type, searchen)

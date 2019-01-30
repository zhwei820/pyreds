#!/usr/bin/env python

from pyreds.rclient import _redis_client, create_client
from pyreds.stopwords import stopwords
import redis
import jieba

types = {
    'intersect': 'zinterstore',
    'union': 'zunionstore',
    'and': 'zinterstore',
    'or': 'zunionstore'
}


def create_search(key):
    if not key:
        raise ValueError('create_search() requires a redis key for namespacing.')

    return Search(key)


# Return the words in `str`.
def _words(s):
    return jieba.cut_for_search(s)


# Strip stop words in `words`.
def _strip_stopwords(words):
    ret = []

    if not words:
        return ret

    for word in words:
        if word in stopwords:
            continue
        ret.append(word)

    return ret


# Return an object mapping each word in a list
# to the number of times it occurs in the list.
def _count_words(words):
    mapper = {}

    if not words:
        return mapper

    for word in words:
        if word not in mapper:
            mapper[word] = 1
        else:
            mapper[word] += 1

    return mapper


# Initialize a new `Query` with the given `str`
# and `search` instance.
class Query:

    def __init__(self, txt, type, search):
        self.txt = txt
        self.type(type if type else 'and')
        self.between(0, -1)
        self.search = search

    # Set `type` to "union" or "intersect", aliased as
    # "or" and "and".

    def type(self, type):
        self._type = types[type] if type and type in types else types['and']
        return self

    # Limit search to the specified range of elements.
    def between(self, start, stop):
        self._start = start
        self._stop = stop
        return self

    # Perform the query
    def end(self):
        key = self.search.key
        db = self.search.client
        query = self.txt
        words = _strip_stopwords(_words(query))
        keys = [key + ':word:' + word for word in words]
        type = self._type
        start = self._start
        stop = self._stop

        if not len(keys):
            return []

        # keys = [key.encode('utf-8') for key in keys]

        tkey = key + 'tmpkey'
        pipe = db.pipeline()
        getattr(pipe, type)(tkey, keys)
        for cmd in [
            ['zrevrange', tkey, start, stop],
            ['zremrangebyrank', tkey, start, stop]
        ]:
            getattr(pipe, cmd[0])(*cmd[1:])

        ids = pipe.execute()
        return ids[1]


# Initialize a new `Search` with the given `key`.
class Search:

    def __init__(self, key):
        self.key = key
        self.client = create_client()

    # Index the given `str` mapped to `id`
    def index(self, txt, id):
        key = self.key
        db = self.client
        words = _strip_stopwords(_words(txt))
        counts = _count_words(words)
        keys = words

        cmds = []
        for k in keys:
            # k = k.encode('utf-8').decode()
            cmds.append(['zadd', key + ':word:' + k, counts[k], id])
            cmds.append(['zadd', key + ':object:' + str(id), counts[k], k])

        pipe = db.pipeline()
        for cmd in cmds:
            getattr(pipe, cmd[0])(*cmd[1:])

        return pipe.execute()

    # to remove index
    def remove(self, id):
        key = self.key
        db = self.client

        constants =  db.zrevrangebyscore(key + ':object:' + str(id), '+inf', 0)

        pipe = db.pipeline()
        pipe.delete(key + ':object:' + str(id))

        for c in constants:
            pipe.zrem(key + ':word:' + c.decode('utf-8'), id)

        return pipe.execute()

    # Perform a search on the given `query` returning
    # a `Query` instance.
    def query(self, txt, type = None):
        return Query(txt, type, self)

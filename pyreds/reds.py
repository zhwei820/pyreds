#!/usr/bin/env python

from pyreds.rclient import create_client


def create_search(key):
    if not key:
        raise ValueError('create_search() requires a redis key for namespacing.')

    return Search(key)


# Initialize a new `Search` with the given `key`.
class Search:

    def __init__(self, key):
        self.key = key
        self.client = create_client()

    # Index the given `str` mapped to `id`
    def index(self, txt, id):
        # ch
        return

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

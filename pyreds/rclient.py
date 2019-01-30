# coding: utf-8
# 19-1-30 下午2:02

import redis

_redis_client = None


def set_client(in_client):
    global _redis_client
    _redis_client = in_client


def create_client():
    global _redis_client
    if not _redis_client:
        _redis_client = redis.StrictRedis()
    return _redis_client

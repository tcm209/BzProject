# -*- coding: utf-8 -*-
import redis

#redis操作
class RedisTools(object):

    def __init__(self):
        pool=redis.ConnectionPool(host='127.0.0.1',port=6379)
        self.r=redis.Redis(connection_pool=pool)

    def get_redis(self):
        return self.r




if __name__=="__main__":
    re=RedisTools()
    r=re.get_redis()
    r.set("name1","hhelo")

    print(r.get("name1"))





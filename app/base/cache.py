from redis import StrictRedis
from settings import REDIS_HOST, REDIS_PORT


class RedisCache:
    def __init__(self, prefix):
        self.prefix = prefix
        self.redis = StrictRedis(REDIS_HOST, REDIS_PORT, 0)

    def get(self, key):
        return self.redis.get(self.prefix + str(key))

    def set(self, key, value, expire=0):
        redis_key = self.prefix + str(key)
        self.redis.set(redis_key, value)
        if expire > 0:
            self.redis.expire(redis_key, expire)
        return value

    def delete(self, key):
        self.redis.delete(self.prefix + str(key))

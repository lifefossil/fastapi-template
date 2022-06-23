import aioredis
from aioredis import Redis
from src.database.dbconfig import redisconfig


# async def sys_cache() -> Redis:
#     cache_pool = aioredis.ConnectionPool.from_url(
#         f"redis://{redisconfig.get('default').host}:{redisconfig.get('default').port}",
#         db=redisconfig.get('default').database,
#         encoding=redisconfig.get('default').encoding,
#         decode_responses=True
#     )
#     return Redis(connection_pool=cache_pool)


class Cache:
    """
    缓冲操作类
    """

    def __init__(self):
        self.cache_pool = aioredis.ConnectionPool.from_url(
            f"redis://{redisconfig.get('default').host}:{redisconfig.get('default').port}",
            db=redisconfig.get('default').database,
            encoding=redisconfig.get('default').encoding,
            password=redisconfig.get('default').password,
            decode_responses=True
        )
        self.redis: Redis | None = None

    async def get_redis(self) -> Redis:
        if self.redis:
            return self.redis
        self.redis = await Redis(connection_pool=self.cache_pool)
        return self.redis

    async def close_cache(self):
        if self.redis:
            await self.redis.close()


# 实例化, 实现单例模式
cache = Cache()


async def sys_cache() -> Redis:
    """
    获得系统本地缓存
    :return: Redis
    """
    return await cache.get_redis()


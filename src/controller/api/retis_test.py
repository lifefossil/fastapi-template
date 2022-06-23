from fastapi import APIRouter, Depends
from aioredis import Redis
from src.database.redisdb import sys_cache

router = APIRouter()


@router.get("/test/redis")
async def redis(redis: Redis = Depends(sys_cache)):
    await redis.set(name="name", value="oliver", ex=60)
    return 'ok'

# @router.get("/test/redis")
# async def redis():
#     redis = await sys_cache()
#     print("hello")
#     await redis.set(name="name", value="oliver", ex=60)
#     return 'ok'

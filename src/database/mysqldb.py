from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.database.dbconfig import mysqlconfig




# -----------------------数据库配置-----------------------------------
DB_ORM_CONFIG = {
    "connections": {
        "base": {
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': mysqlconfig.get('default').host,
                'user': mysqlconfig.get('default').username,
                'password': mysqlconfig.get('default').password,
                'port': mysqlconfig.get('default').port,
                'database': mysqlconfig.get('default').database,
            }
        },
    },
    "apps": {
        "base": {"models": ["src.model.admin"], "default_connection": "base"},

    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}


async def register_mysql(app: FastAPI):
    # 注册数据库
    register_tortoise(
        app,
        config=DB_ORM_CONFIG,
        generate_schemas=False,
        add_exception_handlers=True,
    )
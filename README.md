# 模板使用说明
## 安装
该项目采用 `poetry` 管理项目依赖和虚拟环境, 将项目拉取到本地后:
```shell
> cd fastapi-template
# 创建虚拟环境
> python -m venv venv
# 激活虚拟环境
> venv/Script/active
# 安装 `poetry`
> pip install poetry
# 安装项目依赖
> poetry install
```

## 配置数据库
在项目根目录application.yaml中新增数据库配置:
```yaml
# 如果项目只需要用到一个数据库
datasource:
    mysql: 
        name: default
        driver: mysqlclient
        username: root
        password: 123
        host: localhost
        port: 3306
        database: test
        encode: utf-8
        timezone: Asia/Shanghai
        unicode: True
        
# 如果项目用到两个或者两个以上数据库
#datasource:
#    mysql:
#        -
#            name: db1
#            driver: mysqlclient
#            username: root
#            password: 123
#            host: 192.168.1.2
#            port: 3306
#            database: user
#            encode: utf-8
#        -
#            name: db2
#            driver: mysqlclient
#            username: root
#            password: 123
#            host: 192.168.1.3
#            port: 3306
#            database: admin
#            encode: utf-8
```
然后在 `src/database/mysqldb.py` 中注册新增的数据库, 获得数据库信息, 是根据 `name` 参数来获取. 
比如两个数据库要获取db1数据的host可以这样:

```python
from src.database.dbconfig import mysqlconfig

print(mysqlconfig.get('db1').host)
```
## 运行项目
```shell
> poetry run dev 
```

## 访问项目
```shell
visit: http://127.0.0.1:8000/docs
```

## 文件和文件夹说明
项目主入口: `src/main.py`
```shell
|
- docs    # 存放模板使用说明
|
- resources   # 存放静态资源和html模板
|
- src    # 编写项目主要代码位置
|   |
|   - controller    # api和视图
|   |
|   - core    # 项目核心功能代码集合
|   |
|   - database    # 数据库操作
|   |
|   - exception   # 异常处理
|   |
|   - middleware    # 中间件
|   |
|   - model   # 映射到数据库表的实例模型
|   |
|   - router    # 项目路由
|   |
|   - util    # 工具
|   |
|   - main.py   # 项目入口
|
- application.yaml    # 项目配置文件, 配置参数参考: docs/config/application.md
|
- fastapicf.py    # fastapi 配置文件
|
- requirements.txt    # 项目依赖文件
|
```
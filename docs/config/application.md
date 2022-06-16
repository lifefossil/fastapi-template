# application.yaml 配置
---
application.yaml 配置参数:
```yaml
app:
  env: dev
  entry: src/router.py
  oss:
    access_key: xxx
    secret_key: xxx
    bucket: xxx
    secure: True
  datasource:
    mysql:
      driver: mysqlclient
      username: xxx
      password: xxx
      host: xxx
      port: xxx
      database: xxx
      encode: utf-8
      timezone: Asia/Shanghai
      unicode: True
    mongodb:
      host: xxx
      port: xxx
      database: xxx
      authentication-database: xxx
      username: xxx
      password: xxx
  redis:
    database: 0
    host: xxx
    port: xxx
    password: xxx
```
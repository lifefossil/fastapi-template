# 模板使用说明
---
## 安装
模板拷贝到本地后, 运行下面命令安装依赖(最好新建虚拟环境)
```shell
> cd fastapi-template
# 创建虚拟环境
> python -m venv venv
# 激活虚拟环境
> venv/Script/active
# 安装依赖
> pip install -r requirements.txt
```

## 运行项目
```shell
> uvicorn src.main:app --reload  
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
- modules   # 插件功能模块
|
- src    # 编写项目主要代码位置
|   |
|   - controller    # api和视图
|   |
|   - core    # 项目核心功能代码集合
|   |
|   - exception   # 异常处理
|   |
|   - middleware    # 中间件
|   |
|   - model   # 映射到数据库表的实例模型
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
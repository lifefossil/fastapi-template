from src.core.AppConfig import appconfig


class Mysqldb:
    """
    application.yaml -> datasource -> mysql
    定义数据库默认参数
    """

    def __init__(self, _dict: dict | None = None):
        self.username: str = 'root'
        self.password: str = ''
        self.host: str = 'localhost'
        self.port: int = 3306
        self.database: str = ''
        self.timezone: str = 'Asia/Shanghai'
        self.encode: str = 'UTF-8'
        self.unicode: bool = True
        self.driver: str = 'mysqlclient'
        self.name: str = 'default'
        if _dict:
            self.__dict__.update(_dict)


def get_all_mysql_config() -> dict[str, Mysqldb]:
    result: dict[str, Mysqldb] = dict()
    try:
        mysqls = appconfig.config.get('datasource').get('mysql')
        if mysqls and isinstance(mysqls, dict):
            result[mysqls.get('name')] = Mysqldb(mysqls)
            return result
        if mysqls and isinstance(mysqls, list):
            for mysql in mysqls:
                result[mysql.get('name')] = Mysqldb(mysql)
            return result
    except Exception as e:
        pass
    return result


mysqlconfig = get_all_mysql_config()

if __name__ == '__main__':
    result = get_all_mysql_config()
    print(result.get('default').host)

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


def _parse(c: dict) -> dict[str, Mysqldb]:
    mysqldb = Mysqldb(c)
    return {mysqldb.name: mysqldb}


def get_all_mysql_config() -> list[dict[str, Mysqldb]]:
    result = list()
    try:
        mysqls = appconfig.config.get('datasource').get('mysql')
        if mysqls and isinstance(mysqls, dict):
            result.append(_parse(mysqls))
            return result
        if mysqls and isinstance(mysqls, list):
            for mysql in mysqls:
                result.append(_parse(mysql))
            return result
    except Exception as e:
        pass
    return result


mysqlconfig = get_all_mysql_config()

if __name__ == '__main__':
    result = get_all_mysql_config()
    for item in result:
        for k, v in item.items():
            print(k, v.host)

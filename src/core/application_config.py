from yaml import safe_load
from pathlib import Path
from modules.logger import console_logger as logger

BASE_DIR: Path = Path(__file__).parent.parent.parent






class Oss:
    """
    application.yaml
    定义配置文件OSS对象默认参数
    """
    domain: str = 'localhost'
    access_key: str = 'admin'
    secret_key: str = 'admin'
    port: int = 9000
    bucket: str = ''
    secure: bool = False

    def __init__(self, _dict: dict | None):
        if _dict:
            self.__dict__.update(_dict)


class App:
    env: str | None = None
    entry: str = 'src/main.py'

    def __init__(self, _dict: dict | None):
        if _dict:
            self.__dict__.update(_dict)


class Application:
    mysql: Database = Database(None)
    mongodb: Database = None
    oss: Oss = Oss(None)
    app: App = App(None)

    def __init__(self, appConfigPath: str | None = None):
        self.custom_app_path = appConfigPath
        self._application_path: str | None = None
        self._dev_application_path: str | None = None
        self._prod_application_path: str | None = None
        # 初始化路径
        self._init_app_path()

        # 根据路径指引的配置文件, 初始化类属性
        self._init_application()

        # 2. 根据开启的配置进行该配置合并
        self._merge_prod_or_dev()

    def _init_app_path(self):
        """
        初始化和处理配置文件路径
        :return: None
        """
        dev_path = BASE_DIR.joinpath('application-dev.yaml')
        prod_path = BASE_DIR.joinpath('application-prod.yaml')
        app_path = BASE_DIR.joinpath('application.yaml')
        if dev_path.exists():
            self._dev_application_path = dev_path
        if prod_path.exists():
            self._prod_application_path = prod_path
        if self.custom_app_path is None:
            if app_path.exists():
                self._application_path = app_path
        else:
            cp = Path(self.custom_app_path)
            if cp.exists():
                self._application_path = cp
            else:
                logging.error("你提供的 application.yaml 地址找不到: {}, 并使用默认配置".format(cp))

    def _merge_prod_or_dev(self):
        if self.app.env == 'dev':
            if self._dev_application_path is not None:
                try:
                    with open(self._dev_application_path, 'r', encoding='utf8') as f:
                        app_dict: dict = safe_load(f)
                        self._update(app_dict)
                except Exception as e:
                    logging.error("打开配置文件application-dev.yaml失败", e)
        elif self.app.env == 'prod':
            if self._prod_application_path is not None:
                try:
                    with open(self._prod_application_path, 'r', encoding='utf8') as f:
                        app_dict: dict = safe_load(f)
                        self._update(app_dict)
                except Exception as e:
                    logging.error("打开配置文件application-prod.yaml失败", e)
        else:
            pass

    def _update(self, config: dict | None = None):
        if config is not None:
            self.oss.__init__(config.get('oss', None))
            self.database.__init__(config.get('oss', None))

    def _init_application(self):
        if self._application_path is not None:
            try:
                with open(self._application_path, 'r', encoding='utf8') as f:
                    app_dict: dict = safe_load(f)
                    self._inject(app_dict)
            except Exception as e:
                logging.error("打开配置文件application.yaml失败", e)

    def _inject(self, config: dict | None = None):
        if config is not None:
            self.database = Database(config.get('database', None))
            self.oss = Oss(config.get('oss', None))
            self.app = App(config.get('app', None))


application_config: Application = Application()

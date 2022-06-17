from yaml import safe_load
from pathlib import Path
from src.core.logger import console_logger as logger
from src.util.path_util import parse_user_home_path
from src.util.dict_util import deep_merge

BASE_DIR: Path = Path(__file__).parent.parent.parent


class AppConfig:

    def __init__(self, custom_app_path: str | None = None):
        self._application_path: str | None = None
        self._external_config_path: Path | None = None
        # 项目配置信息
        self.inconfig: dict = dict()
        # 项目中引入的配置信息
        self.exconfig: dict = dict()
        # 合并后的配置信息
        self.config: dict = dict()
        # 初始化路径
        self._init_app_path(custom_app_path)
        # 合并config 和 exconfig, 如果由冲突最终以config为主
        self._merge_exconfig_config()
        # 根据app.env开启生产环境
        self._is_prod()

    def _merge_exconfig_config(self):
        """
        将exconfig 和 inconfig中的配置信息进行合并, 若有冲突最终以inconfig为主
        :return: None
        """
        self.config = deep_merge(self.exconfig, self.inconfig)

    def _init_app_path(self, custom_app_path):
        """
        初始化和处理配置文件路径
        :return: None
        """

        # 获取 真实application.yaml地址
        app_path = BASE_DIR.joinpath('application.yaml')
        if custom_app_path is None:
            if app_path.exists():
                self._application_path = app_path
            else:
                logger.warn('没有找到application.yaml配置文件')
        else:
            cp = Path(custom_app_path)
            if cp.exists():
                self._application_path = cp
            else:
                logger.error("你提供的 application.yaml 地址找不到: {}, 并使用默认配置".format(cp))

        # 获取 application.yaml 配置信息到 self.inconfig
        if self._application_path is not None:
            try:
                with open(self._application_path, 'r', encoding='utf8') as f:
                    self.inconfig = safe_load(f)
            except Exception as e:
                logger.error("打开配置文件application.yaml失败", e)

        # 获取 app.include 地址
        try:
            include_path = self.inconfig.get('app').get('include')
            if include_path:
                self._external_config_path = parse_user_home_path(include_path)
        except Exception as e:
            logger.info('未发现在application.yaml中配置app.include')

        # 将外部配置文件信息写入 self.exconfig 中
        if self._external_config_path and self._external_config_path.exists():
            try:
                with open(self._external_config_path, 'r', encoding='utf8') as f:
                    self.exconfig = safe_load(f)
            except Exception as e:
                logger.error("打开app.include中的外部配置文件失败, 地址{}".format(self._external_config_path), e)

    def _is_prod(self):
        """
         todo 处理 app.env = prod
        """
        pass

appconfig: AppConfig = AppConfig()

if __name__ == '__main__':
    config = AppConfig()
    print(config.config)

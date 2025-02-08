from dishka import Provider, Scope, provide

from app.settings.database.database_settings import DatabaseSettings
from app.settings.factory import SettingsFactory


class ConfigProvider(Provider):
    @provide(scope=Scope.APP, provides=SettingsFactory)
    def get_config(self) -> SettingsFactory:
        return SettingsFactory()

    @provide(scope=Scope.APP)
    def get_db_config(self, cfg_factory: SettingsFactory) -> DatabaseSettings:
        return cfg_factory.database_settings

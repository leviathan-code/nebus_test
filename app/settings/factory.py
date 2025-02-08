from app.settings.database.database_settings import DatabaseSettings


class SettingsFactory:
    def __init__(self) -> None:
        self.database_settings = DatabaseSettings()
